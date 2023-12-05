from lib0.QIterable import QIterable
from lib0.list_utils import q_count


class QList:
    def __init__(self, x: list, enclose_parentheses: bool = False):
        self.x = x
        self.enclose_parentheses = enclose_parentheses

    def __str__(self) -> str:
        res = ";".join([str(e) for e in self.x])
        if self.enclose_parentheses:
            return "(" + res + ")"
        return res

    @staticmethod
    def parse(s):
        raise "Not Implemented"

    def count(self) -> str:
        return q_count(str(self))

    def foreach(self) -> QIterable:
        return QIterable(str(self))
