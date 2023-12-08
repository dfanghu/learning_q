from lib_q.QList import QList
from lib_q.QSym import QSym
from lib_q.QVec import QVec, QIndexable
from lib_q.list_utils import q_flip


class QDictionary(QIndexable):
    def __init__(self, x: dict, parentheses: bool = False):
        super().__init__(x)
        self.x = x
        self.parentheses = parentheses

    def __str__(self) -> str:
        res = "".join([str(QSym(k)) for k in self.x.keys()]) + "!" + str(
            QList([QVec(v) for v in self.x.values()], parentheses=True))
        if self.parentheses:
            return "(" + res + ")"
        return res

    def single_row_vector(self) -> str:
        res = "".join([str(QSym(k)) for k in self.x.keys()]) + "!" + str(QVec(list(self.x.values())))
        if self.parentheses:
            return "(" + res + ")"
        return res

    def flip(self) -> str:
        return q_flip(str(self))
