from lib_q.lang_utils import q_cmd, q_f


def q_exit_cli() -> str:
    return r"\\"


def q_list_tables() -> str:
    return q_cmd("a", [])


def q_today() -> str:
    return q_cmd("date", [])


def q_os(cmd: str) -> str:
    return q_f("system", [cmd])
