from datetime import datetime

from lib_q.QExpression import QExpression


class QDate(QExpression):
    def __init__(self, x: datetime):
        self.x = x

    def __str__(self):
        return self.x.strftime("%Y.%m.%d")

    @staticmethod
    def parse(s):
        try:
            return datetime.strptime(s, "%Y.%m.%d")
        except:
            return None
