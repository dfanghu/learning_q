from lib0.QIterable import QIterable
from lib0.list_utils import q_count


class QString:
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return "\"" + self.x + "\""

    def count(self) -> str:
        return q_count(str(self))

    def foreach(self) -> QIterable:
        return QIterable(str(self))
