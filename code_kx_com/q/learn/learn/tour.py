from lib.array_utils import *
from lib.file_utils import *
from lib.lang_utils import q_assign, q_guessExpr
from lib.mem_utils import *
from lib.trig_utils import *
from lib.web_utils import q_download_csv
from lib.sql_utils import *


def all_tests():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


def test1():
    assert "2+2 3 4" == q_add(2, [2, 3, 4])


def test2():
    assert "acos -1" == q_acos(-1)


def test3():
    assert r"\l sp.q" == q_load_file_or_dir("sp.q")


def test4():
    assert r"\a" == q_list_tables()


def test5():
    assert r"save `:path/to/sp" == q_save("path/to", "sp")
    assert r"save `:path/to/sp.xls" == q_save("path/to", "sp", "xls")
    assert r"save `:sp" == q_save("", "sp")


def test6():
    url_expr = q_guessExpr("https://code.kx.com/download/data/example.csv")
    res = q_assign("url", url_expr)
    print(res)
    assert res == f'''url:"https://code.kx.com/download/data/example.csv"'''

    res2 = q_download_csv("url", coltypes="SFI", sep=",", header=True)
    print(res2)
    assert res2 == '''("SFI";enlist",")0: system \"curl -Ls \",url'''

    res3 = q_count(q_assign("t", res2))
    print(res3)
    assert res3 == '''count t:("SFI";enlist",")0: system \"curl -Ls \",url'''

    res4 = q_save("", "t", "csv", "example")
    print(res4)
    assert res4 == '''`:example.csv set t'''


def test7():
    res = q_select_all_from_where("sp", q_logical_test_gt("qty", "200"))
    print(res)
    assert '''select from sp where qty > 200''' == res

    res2 = q_update_from_where(q_assign("qty", q_mul("qty", "2")), "sp", q_logical_test_eq("p", q_symbol("p2")))
    print(res2)
    assert '''update qty:qty*2 from sp where p = `p2''' == res2
