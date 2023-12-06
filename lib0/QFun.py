from lib0.QList import QList
from lib0.lang_utils import q_assign


class QFun:
    def __init__(self, body, name: str = "", argv: list = None):
        self.argv = argv
        self.body = body
        self.name = name

    def __str__(self):
        if self.name != "":
            return self.name
        res = self.body
        if self.argv is not None:
            res = f"[{QList(self.argv, enclose_parentheses=False)}]" + res
        res = "{" + res + "}"
        return res

    def assign_to_name(self, name) -> str:
        return q_assign(name, str(self))

    def call(self, argsin, enclose_brackets: bool = False):
        head = self.name if self.name != "" else str(self)
        if enclose_brackets:
            return f"{head}[{argsin}]"
        sep = " " if not head.endswith("}") else ""
        return f"{head}{sep}{argsin}"

    def map(self, iterable):
        return f"{self} each {iterable}"

    def accum(self, initial, rest, intermediate_steps=False):
        op = "\\" if intermediate_steps else "/"
        return f"{initial} {self}{op} {rest}"

    def do_n_times(self, n, initial, intermediate_steps=False):
        op = "\\" if intermediate_steps else "/"
        return f"{n} {self}{op}{initial}"
