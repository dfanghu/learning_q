from lib_q.QExpression import QExpression


class QAmend(QExpression):
    def __init__(self, v, expr):
        self.v = v
        self.expr = expr

    def __str__(self):
        return f"{self.v}:{self.expr}"
