import re

from lib_q.QAmend import QAmend


def q_f(head: str, tail: list) -> str:
    return f"""{head} {' '.join([str(e) for e in tail])}""".strip()


def q_infix(op: str, lhs: str, rhs: str) -> str:
    return " ".join([lhs, op, rhs])


def q_cmd(head: str, tail: list) -> str:
    return q_f("\\" + head, tail)


def q_is_symbol(s) -> bool:
    try:
        return isinstance(s, str) and re.match("`[^`]+$", s) is not None
    except:
        return False


def q_assign(v: str, expr) -> QAmend:
    return QAmend(v, expr)


def q_parentheses(x) -> str:
    return f"({x})"


def q_brakets(x) -> str:
    return f"[{x}]"


def q_brackets(x) -> str:
    return f"[{x}]"


def q_braces(x) -> str:
    return "{" + str(x) + "}"


def q_vectorize_one_of_two_params(f, fixed, fix_first=False, repeat: int = 1):
    if fix_first:
        a = fixed
    else:
        a = f";{fixed}"
    res = f"{f}[{a}]/ "
    if repeat > 1:
        res = f"{repeat} {res}"
    return res
