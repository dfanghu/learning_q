from lib0.lang_utils import q_f


def q_range(n: int) -> str:
    return q_f('til', [n])


def q_concat2(x, y) -> str:
    return f"{x},{y}"


def q_concat(x: list) -> str:
    return ",".join([str(el) for el in x])


def q_count(expr) -> str:
    return q_f("count", [expr])


def q_show(expr) -> str:
    return q_f("show", [expr])


def q_enlist(expr) -> str:
    return q_f("enlist", [expr])


def q_flip(x: str) -> str:
    return q_f("flip", [x])


def q_binop(lhs, op: str, rhs, space: bool) -> str:
    sep = " " if space else ""
    return f"{lhs}{sep}{op}{sep}{rhs}"


def q_logical_test_gt(lhs, rhs, space: bool = False) -> str:
    return q_binop(lhs, ">", rhs, space=space)


def q_logical_test_ge(lhs, rhs, space: bool = False) -> str:
    return q_binop(lhs, ">=", rhs, space=space)


def q_logical_test_eq(lhs, rhs, space: bool = False) -> str:
    return q_binop(lhs, "=", rhs, space=space)


def q_logical_test_neq(lhs, rhs, space: bool = False) -> str:
    return q_binop(lhs, "<>", rhs, space=space)


def q_logical_test_lt(lhs, rhs, space: bool = False) -> str:
    return q_binop(lhs, "<", rhs, space=space)


def q_logical_test_le(lhs, rhs, space: bool = False) -> str:
    return q_binop(lhs, "<=", rhs, space=space)


def q_add(x, y, space: bool = False) -> str:
    return q_binop(x, "+", y, space=space)


def q_subtract(x, y, space: bool = False) -> str:
    return q_binop(x, "-", y, space=space)


def q_mul(x, y, space: bool = False) -> str:
    return q_binop(x, "*", y, space=space)


def q_div(x, y, space: bool = False) -> str:
    return q_binop(x, "%", y, space=space)
