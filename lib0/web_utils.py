from lib0.array_utils import q_concat
from lib0.file_utils import q_load_csv
from lib0.mem_utils import q_os


def q_download(url_expr: str) -> str:
    return q_os(q_concat('"curl -Ls "', url_expr))


def q_download_csv(url_expr: str, coltypes: str, sep: str = ",", header: bool = False) -> str:
    return q_load_csv(q_download(url_expr), coltypes, sep=sep, header=header)
