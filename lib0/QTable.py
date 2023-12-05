from lib0.QList import QList
from lib0.QSymbol import QSymbol
from lib0.QVector import QVector
from lib0.list_utils import q_flip, q_count, QIterable


class QDictionary:
    def __init__(self, x: dict, enclose_parentheses: bool = False):
        self.x = x
        self.enclose_parentheses = enclose_parentheses

    def __str__(self) -> str:
        res = "".join([str(QSymbol(k)) for k in self.x.keys()]) + "!" + str(
            QList([QVector(v) for v in self.x.values()]))
        if self.enclose_parentheses:
            return "(" + res + ")"
        return res

    @staticmethod
    def parse(s):
        raise "Not Implemented"

    def flip(self) -> str:
        return q_flip(str(self))

    def count(self) -> str:
        return q_count(str(self))

    def foreach(self) -> QIterable:
        return QIterable(str(self))
