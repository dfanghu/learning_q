from datetime import datetime

from lib_q.QExpression import QExpression


class QMonth(QExpression):
    def __init__(self, x: datetime):
        self.x = x

    def __str__(self):
        return self.x.strftime("%Y.%m") + "m"

    @staticmethod
    def parse(s):
        try:
            if len(s) != 6 or not s.endswith("m"):
                return False
            return datetime.strptime(s[:-1], "%Y.%m")
        except:
            return None
