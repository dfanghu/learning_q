from lib_q.list_utils import *
from lib_q.file_utils import *
from lib_q.QStr import QStr


def all_tests():
    test1()
    test2()
    test3()
    test4()


def test1():
    assert "read0 `:path/to/example.csv" == q_read_lines("path/to/example.csv")


def test2():
    res = q_show(q_assign("t", q_load_csv(
        file_stream=q_filesymbol("path/to/example.csv"), coltypes="SFI", header=True, sep=",")))
    print(res)
    assert '''show t:("SFI";enlist",")0: `:path/to/example.csv''' == res


def test3():
    res = q_prepare_text(r"\t", "t")
    print(res)
    assert r'"\t"' + " 0: t" == res


def test4():
    res = q_save_text(q_filesymbol("test.txt"), q_enlist(QStr("text to save")))
    print(res)
    assert '''`:test.txt 0: enlist "text to save"''' == res
