from lib_q.QExpression import QExpression
from lib_q.list_utils import q_count


class QCountable(QExpression):
    def __init__(self, x):
        self.x = x

    def __str__(self) -> str:
        return str(self.x)

    def count(self) -> str:
        return q_count(str(self))


class QIterable(QCountable):
    def __init__(self, x):
        super().__init__(x)
        self.x = x

    def __str__(self) -> str:
        tail = str(self.x)
        sep = "" if tail[0] in "([{" else " "
        return f"each{sep}{tail}"

    @staticmethod
    def parse(s):
        raise "Not Implemented"

    def foreach(self):
        return QIterable(str(self))
