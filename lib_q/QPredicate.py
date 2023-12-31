from lib_q.QExpression import QExpression


class QPredicate(QExpression):
    def __init__(self, x):
        self.x = x

    def __str__(self):
        return str(self.x)

    def index_where(self):
        return f"where {self}"
