from lib_q.QVec import QIndexable


class QStr(QIndexable):
    def __init__(self, x: str):
        super().__init__(x)
        self.x = x

    def __str__(self):
        return "\"" + self.x + "\""
