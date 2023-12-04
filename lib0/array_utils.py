from lib0.lang_utils import q_f


def q_range(n: int) -> str:
    return q_f('til', [n])




def q_concat(expr1, expr2) -> str:
    return expr1 + "," + expr2


def q_count(expr) -> str:
    return q_f("count", [expr])


def q_show(expr) -> str:
    return q_f("show", [expr])


def q_enlist(expr: str) -> str:
    return q_f("enlist", [expr])
