def q_f(head: str, tail: list) -> str:
    return f"""{head} {' '.join([str(e) for e in tail])}"""
