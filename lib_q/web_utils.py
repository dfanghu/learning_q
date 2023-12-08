from lib_q.list_utils import q_concat2
from lib_q.file_utils import q_load_csv
from lib_q.mem_utils import q_os


def q_download(url_expr: str) -> str:
    return q_os(q_concat2('"curl -Ls "', url_expr))


def q_download_csv(url_expr: str, coltypes: str, sep: str = ",", header: bool = False) -> str:
    return q_load_csv(q_download(url_expr), coltypes, sep=sep, header=header)


def q_server_start(host: str, port: str) -> str:
    return f"q -p {host}:{port}"
