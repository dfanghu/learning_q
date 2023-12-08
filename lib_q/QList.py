from lib_q.QVec import QIndexable


class QList(QIndexable):
    def __init__(self, x, parentheses: bool = False):
        if not isinstance(x, list):
            x = [x]
        super().__init__(x)
        self.parentheses = parentheses

    def __str__(self) -> str:
        res = ";".join([str(e) for e in self.x])
        if self.parentheses:
            return "(" + res + ")"
        return res
