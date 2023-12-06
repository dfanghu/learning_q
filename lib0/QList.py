from lib0.QVec import QIndexable


class QList(QIndexable):
    def __init__(self, x: list, enclose_parentheses: bool = False):
        super().__init__(x)
        self.enclose_parentheses = enclose_parentheses

    def __str__(self) -> str:
        res = ";".join([str(e) for e in self.x])
        if self.enclose_parentheses:
            return "(" + res + ")"
        return res
