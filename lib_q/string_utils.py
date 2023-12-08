from lib_q.lang_utils import q_f


def q_string(expr: str) -> str:
    return q_f("string", [expr])


