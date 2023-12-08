from lib_q.QExpression import QExpression
from lib_q.lang_utils import q_is_symbol


class QSym(QExpression):
    def __init__(self, x: str):
        self.x = x

    def __str__(self):
        return "`" + self.x

    @staticmethod
    def parse(s):
        if q_is_symbol(s):
            return QSym(s[1:])
        return None
