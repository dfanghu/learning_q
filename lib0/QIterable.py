from lib0.list_utils import q_count


class QCountable:
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
        return f"each {self.x}"

    @staticmethod
    def parse(s):
        raise "Not Implemented"

    def foreach(self):
        return QIterable(str(self))
