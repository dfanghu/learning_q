from lib0.QBoolFlags import QBoolFlags
from lib0.QIterable import QIterable
from lib0.QSym import QSym


class QIndexable(QIterable):

    def __init__(self, x):
        super().__init__(x)
        self.x = x

    def __str__(self):
        return str(self.x)

    def indexing(self, indexes: list, enclose_brackets: bool = True) -> str:
        if enclose_brackets:
            return f"{self}[{QVec(indexes)}]"
        else:
            return f"{self} {QVec(indexes)}"

    def where(self, flags: QBoolFlags):
        return f"{self} where {flags}"

    def head(self, length: int):
        return f"{length - 1}#{self.x}"

    def tail(self, length: int):
        return f"-{length}#{self.x}"

    def mid(self, begin: int, length: int):
        return f"{begin} {length} sublist {self.x}"


class QVec(QIndexable):
    def __init__(self, x, enclose_brackets: bool = False):
        if not isinstance(x, list):
            x = [x]
        super().__init__(x)
        self.enclose_brackets = enclose_brackets

    def __str__(self):
        sep = " "
        if len(self.x) > 0 and isinstance(self.x[0], QSym):
            sep = ""
        res = sep.join([str(x) for x in self.x])
        if self.enclose_brackets:
            return "[" + res + "]"
        return res
