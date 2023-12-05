from datetime import time, datetime


class QTime:
    def __init__(self, x: time):
        self.x = x

    def __str__(self):
        return self.x.strftime("%H:%M:%S.%f")[:-3]

    @staticmethod
    def parse(s):
        try:
            if len(s) != len("23:59:59.000") or not s[-4] == ".":
                return None
            return datetime.strptime(s + "000", "%H:%M:%S.%f")
        except:
            return None
