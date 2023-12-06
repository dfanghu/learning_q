from lib0.QDictionary import QDictionary
from lib0.QVec import QVec, QIndexable
from lib0.lang_utils import q_assign
from lib0.list_utils import q_flip, q_concat2


class QTable(QIndexable):
    def __init__(self, x: dict):
        super().__init__(x)
        self.x = x

    def __repr__(self) -> str:
        return "([]" + ";".join([q_assign(k, QVec(v)) for k, v in self.x.items()]) + ")"

    def flip(self) -> str:
        return q_flip(str(self))

    def append(self, row: QDictionary):
        return q_concat2(str(self), str(row))
