def q_f(head: str, tail: list) -> str:
    return f"""{head} {' '.join([str(e) for e in tail])}""".strip()


def q_infix(op: str, lhs: str, rhs: str) -> str:
    return " ".join([lhs, op, rhs])


def q_cmd(head: str, tail: list) -> str:
    return q_f("\\" + head, tail)


def q_guessExpr(x) -> str:
    if isinstance(x, str):
        return '"' + x + '"'
    else:
        return str(x)


def q_assign(v: str, expr: str) -> str:
    return f"{v}:{expr}"


def q_symbol(s: str) -> str:
    return "`" + s


def q_logial_test(lhs: str, op: str, rhs: str) -> str:
    return f"{lhs} {op} {rhs}"


def q_logical_test_gt(lhs: str, rhs: str) -> str:
    return q_logial_test(lhs, ">", rhs)


def q_logical_test_eq(lhs: str, rhs: str) -> str:
    return q_logial_test(lhs, "=", rhs)


def q_logical_test_lt(lhs: str, rhs: str) -> str:
    return q_logial_test(lhs, "<", rhs)


def q_binop(x, op, y) -> str:
    operands = []
    for z in [x, y]:
        if not isinstance(z, list):
            a = str(z)
        else:
            a = " ".join([str(b) for b in z])
        operands.append(a)
    return op.join(operands)


def q_add(x, y) -> str:
    return q_binop(x, "+", y)


def q_subtract(x, y) -> str:
    return q_binop(x, "-", y)


def q_mul(x, y) -> str:
    return q_binop(x, "*", y)


def q_div(x, y) -> str:
    return q_binop(x, "%", y)
