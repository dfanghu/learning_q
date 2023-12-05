from lib0.lang_utils import q_is_symbol


class QSymbol:
    def __init__(self, x: str):
        self.x = x

    def __str__(self):
        return "`" + self.x

    @staticmethod
    def parse(s):
        if q_is_symbol(s):
            return QSymbol(s[1:])
        return None
