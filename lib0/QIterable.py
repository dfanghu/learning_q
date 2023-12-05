from lib0.list_utils import q_count


class QIterable:
    def __init__(self, x):
        self.x = x

    def __str__(self) -> str:
        return f"each {self.x}"

    @staticmethod
    def parse(s):
        raise "Not Implemented"

    def count(self) -> str:
        return q_count(str(self))
