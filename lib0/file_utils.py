from lib0.lang_utils import *


def q_load_file_or_dir(path: str) -> str:
    return q_cmd("l", [path])


def q_pwd() -> str:
    return q_cmd("pwd", [])


def q_cd(path: str) -> str:
    return q_cmd("cd", [path])


def q_save(parent_dir: str, v: str, ext: str = "", rename_v: str = "") -> str:
    if parent_dir != "" and not parent_dir.endswith("/"):
        parent_dir += "/"
    if ext != "" and not ext.startswith("."):
        ext = "." + ext
    if rename_v == "":
        return q_f("save", [f"`:{parent_dir}{v}{ext}"])
    else:
        return q_infix("set", f"`:{parent_dir}{rename_v}{ext}", v)


def q_save_xls(parent_dir: str, v: str, rename_v: str = "") -> str:
    return q_save(parent_dir, v, "xls", rename_v)


def q_save_csv(parent_dir: str, v: str, rename_v: str = "") -> str:
    return q_save(parent_dir, v, "csv", rename_v)


def q_save_tsv(parent_dir: str, v: str, rename_v: str = "") -> str:
    return q_save(parent_dir, v, "tsv", rename_v)


def q_save_txt(parent_dir: str, v: str, rename_v: str = "") -> str:
    return q_save(parent_dir, v, "txt", rename_v)


def q_save_xml(parent_dir: str, v: str, rename_v: str = "") -> str:
    return q_save(parent_dir, v, "xml", rename_v)


def q_load_csv(file_stream: str, coltypes: str, sep: str = ",", header: bool = False) -> str:
    res = ["(", f"\"{coltypes}\";"]
    if header:
        res.append("enlist")
    if sep in ["csv", "tsv"]:
        sep = " " + sep
    else:
        sep = f"\"{sep}\""
    res.append(sep)
    res.append(")0: ")
    res.append(file_stream)
    return "".join(res)


def q_read_lines(path: str) -> str:
    return q_f("read0", [q_filesymbol(path)])


def q_filesymbol(path: str) -> str:
    return "`:" + path


def q_prepare_text(delimiter: str, v: str) -> str:
    return q_infix("0:", f"\"{delimiter}\"", v)


def q_save_text(filesymbol: str, strings: str) -> str:
    return q_infix("0:", filesymbol, strings)
