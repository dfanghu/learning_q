from lib0.QIterable import QIterable
from lib0.QSymbol import QSymbol
from lib0.list_utils import q_count


class QVector:
    def __init__(self, x: list, enclose_square_brackets: bool = False):
        self.x = x
        self.enclose_square_brackets = enclose_square_brackets

    def __str__(self):
        sep = " "
        if len(self.x) > 0 and isinstance(self.x[0], QSymbol):
            sep = ""
        res = sep.join([str(x) for x in self.x])
        if self.enclose_square_brackets:
            return "[" + res + "]"
        return res

    @staticmethod
    def parse(s):
        raise "Not Implemented"

    def count(self) -> str:
        return q_count(str(self))

    def foreach(self) -> QIterable:
        return QIterable(str(self))
