from lib0.lang_utils import q_f


def q_range(n: int) -> str:
    return q_f('til', [n])


def q_concat(expr1, expr2) -> str:
    return expr1 + "," + expr2


def q_count(expr) -> str:
    return q_f("count", [expr])


def q_show(expr) -> str:
    return q_f("show", [expr])


def q_enlist(expr) -> str:
    return q_f("enlist", [expr])


def q_flip(x: str) -> str:
    return q_f("flip", [x])


def q_logial_test(lhs, op: str, rhs) -> str:
    return f"{lhs} {op} {rhs}"


def q_logical_test_gt(lhs, rhs) -> str:
    return q_logial_test(lhs, ">", rhs)


def q_logical_test_eq(lhs, rhs) -> str:
    return q_logial_test(lhs, "=", rhs)


def q_logical_test_lt(lhs, rhs) -> str:
    return q_logial_test(lhs, "<", rhs)


def q_binop(x, op, y) -> str:
    operands = []
    for z in [x, y]:
        operands.append(str(z))
    return op.join(operands)


def q_add(x, y) -> str:
    return q_binop(x, "+", y)


def q_subtract(x, y) -> str:
    return q_binop(x, "-", y)


def q_mul(x, y) -> str:
    return q_binop(x, "*", y)


def q_div(x, y) -> str:
    return q_binop(x, "%", y)
