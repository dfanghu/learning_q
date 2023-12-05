from lib0.QIterable import QIterable
from lib0.QVector import QVector
from lib0.lang_utils import q_assign
from lib0.list_utils import q_flip, q_count


class QTable:
    def __init__(self, x: dict):
        self.x = x

    def __str__(self) -> str:
        return "([]" + ";".join([q_assign(k, QVector(v)) for k, v in self.x.items()]) + ")"

    @staticmethod
    def parse(s):
        raise "Not Implemented"

    def flip(self) -> str:
        return q_flip(str(self))

    def count(self) -> str:
        return q_count(str(self))

    def foreach(self) -> QIterable:
        return QIterable(str(self))
