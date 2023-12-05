import re


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


def q_assign(v: str, expr) -> str:
    return f"{v}:{expr}"
