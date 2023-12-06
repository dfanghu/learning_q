from lib0.QList import QList
from lib0.QSym import QSym
from lib0.QVec import QVec, QIndexable
from lib0.list_utils import q_flip


class QDictionary(QIndexable):
    def __init__(self, x: dict, enclose_parentheses: bool = False):
        super().__init__(x)
        self.x = x
        self.enclose_parentheses = enclose_parentheses

    def __str__(self) -> str:
        res = "".join([str(QSym(k)) for k in self.x.keys()]) + "!" + str(
            QList([QVec(v) for v in self.x.values()], enclose_parentheses=True))
        if self.enclose_parentheses:
            return "(" + res + ")"
        return res

    def single_row_vector(self) -> str:
        res = "".join([str(QSym(k)) for k in self.x.keys()]) + "!" + str(QVec(list(self.x.values())))
        if self.enclose_parentheses:
            return "(" + res + ")"
        return res

    def flip(self) -> str:
        return q_flip(str(self))
