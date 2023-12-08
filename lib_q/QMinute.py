from datetime import time, datetime

from lib_q.QExpression import QExpression


class QMinute(QExpression):
    def __init__(self, x: time):
        self.x = x

    def __str__(self):
        return self.x.strftime("%H:%M")

    @staticmethod
    def parse(s):
        try:
            if len(s) != len("23:59") or s[2] != ":":
                return None
            return datetime.strptime(s, "%H:%M")
        except:
            return None
