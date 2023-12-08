from lib_q.QPredicate import QPredicate
from lib_q.QIterable import QIterable
from lib_q.QSym import QSym


class QIndexable(QIterable):

    def __init__(self, x):
        super().__init__(x)
        self.x = x

    def __str__(self):
        return str(self.x)

    def indexing(self, indexes, brackets: bool = True, outer_parenthesis=False) -> str:
        res = f"{self}[{indexes}]" if brackets else f"{self} {indexes}"
        if outer_parenthesis:
            return f"({res})"
        else:
            return res

    def where(self, flags: QPredicate):
        return f"{self} where {flags}"

    def head(self, length: int):
        return f"{length - 1}#{self.x}"

    def tail(self, length: int):
        return f"-{length}#{self.x}"

    def mid(self, begin: int, length: int):
        return f"{begin} {length} sublist {self.x}"


class QVec(QIndexable):
    def __init__(self, x, brackets: bool = False):
        if not isinstance(x, list):
            x = [x]
        super().__init__(x)
        self.brackets = brackets

    def __str__(self):
        sep = " "
        if len(self.x) > 0 and isinstance(self.x[0], QSym):
            sep = ""
        res = sep.join([str(x) for x in self.x])
        if self.brackets:
            return "[" + res + "]"
        return res

