def q_select_all_from_where(v: str, where: str) -> str:
    return f"select from {v} where {where}"


def q_update_from_where(assignment: str, v: str, where: str) -> str:
    return f"update {assignment} from {v} where {where}"
