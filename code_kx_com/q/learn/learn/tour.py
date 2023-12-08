from lib_q.QOperable import QOperable
from lib_q.QDate import QDate
from lib_q.QDictionary import QDictionary
from lib_q.QFun import QFun
from lib_q.QList import QList
from lib_q.QVec import QVec, QIndexable
from lib_q.list_utils import *
from lib_q.file_utils import *
from lib_q.lang_utils import q_assign
from lib_q.mem_utils import *
from lib_q.QMinute import QMinute
from lib_q.QStr import QStr
from lib_q.QSym import QSym
from lib_q.QTime import QTime
from lib_q.trig_utils import *
from lib_q.web_utils import q_download_csv
from lib_q.sql_utils import *
from datetime import datetime, time


def all_tests():
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()
    test8()
    test9()
    test10()
    test11()
    test12()
    test13()
    test14()
    test15()
    test16()
    test17()


# the-q-session
def test1():
    res = q_add(2, QVec([2, 3, 4]))
    print(res)
    assert "2+2 3 4" == res


def test2():
    assert "acos -1" == q_acos(-1)


# databases
def test3():
    assert r"\l sp.q" == q_load_file_or_dir("sp.q")


def test4():
    assert r"\a" == q_list_tables()


def test5():
    assert r"save `:path/to/sp" == q_save("path/to", "sp")
    assert r"save `:path/to/sp.xls" == q_save("path/to", "sp", "xls")
    assert r"save `:sp" == q_save("", "sp")


def test6():
    url_expr = QStr("https://code.kx.com/download/data/example.csv")
    q_assign("url", url_expr).test('''url:"https://code.kx.com/download/data/example.csv"''')

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
    assert '''select from sp where qty>200''' == res

    res2 = q_update_from_where(q_assign("qty", q_mul("qty", 2)), "sp", q_logical_test_eq("p", QSym("p2")))
    print(res2)
    assert '''update qty:qty*2 from sp where p=`p2''' == res2


# language
def test8():
    res = q_mul(QVec([1, 2, 3]), q_acos(-1))
    print(res)
    assert '''1 2 3*acos -1''' == res

    res2 = QVec([QDate(datetime(2019, 7, 5)),
                 QDate(datetime(2019, 9, 15)),
                 QDate(datetime(2019, 11, 16)), ]).count()
    print(res2)
    assert '''count 2019.07.05 2019.09.15 2019.11.16''' == res2

    res3 = QVec([QMinute(time(hour=8, minute=30)),
                 QMinute(time(hour=12, minute=45)),
                 QMinute(time(hour=17, minute=15)), ]).count()
    print(res3)
    assert '''count 08:30 12:45 17:15''' == res3

    res4 = q_count(QVec([QTime(time(hour=22, minute=45, second=53, microsecond=600000)),
                         QTime(time(hour=22, minute=45, second=53, microsecond=601000)),
                         QTime(time(hour=22, minute=45, second=53, microsecond=602000)), ]))
    print(res4)
    assert '''count 22:45:53.600 22:45:53.601 22:45:53.602''' == res4

    res5 = q_count(QStr("fox"))
    print(res5)
    assert '''count "fox"''' == res5

    res6 = q_count(QList([QStr("quick"), QStr("brown"), QStr("fox")], parentheses=True))
    print(res6)
    assert '''count ("quick";"brown";"fox")''' == res6

    res7 = QList([QStr("quick"), QStr("brown"), QStr("fox")], parentheses=True).foreach().count()
    print(res7)
    assert '''count each("quick";"brown";"fox")''' == res7

    res8 = QVec([QSym("quick"), QSym("brown"), QSym("fox")]).count()
    print(res8)
    assert '''count `quick`brown`fox''' == res8

    res9 = QVec([QSym("quick"), QSym("brown"), QSym("fox")]).foreach().count()
    print(res9)
    assert '''count each `quick`brown`fox''' == res9


def test9():
    res = QList([42, QStr("foxes"), QVec([QSym("screw"), QSym("bolt")]), QDate(datetime(2020, 9, 15))],
                parentheses=True).count()
    print(res)
    assert '''count (42;"foxes";`screw`bolt;2020.09.15)''' == res


def test10():
    res = QVec([3, 1, 4, 5]).count()
    print(res)
    assert '''count 3 1 4 5''' == res

    res = QVec([3, 1, 4, 5.9]).count()
    print(res)
    assert '''count 3 1 4 5.9''' == res

    res = q_count(QStr("jump"))
    print(res)
    assert '''count "jump"''' == res

    res = q_logical_test_lt(QStr("jump"), QStr("n"))
    print(res)
    assert '''"jump"<"n"''' == res

    res = q_add(QDate(datetime(year=2020, month=1, day=1)), QVec([30, 60, 90, 120]))
    print(res)
    assert '''2020.01.01+30 60 90 120''' == res

    res = q_add(QMinute(time(hour=12)), QVec([30, 60, 90, 120]))
    print(res)
    assert '''12:00+30 60 90 120''' == res


def test11():
    res = QStr("abcdef").indexing(QVec([3, 4, 0, 5]))
    print(res)
    assert '''"abcdef"[3 4 0 5]''' == QStr("abcdef").indexing(QVec([3, 4, 0, 5]))


def test12():
    res = QIndexable("sp").indexing(QVec([0, 2]), brackets=False)
    print(res)
    assert '''sp 0 2''' == QIndexable("sp").indexing(QVec([0, 2]), brackets=False)

    res = QIndexable("sp").indexing(QVec([QSym("s"), QSym("p")]), brackets=False)
    print(res)
    assert '''sp `s`p''' == res

    res = QIndexable("sp").indexing(QVec([QSym("qty")]), brackets=True)
    print(res)
    assert '''sp[`qty]''' == res

    res = QOperable(QIndexable("sp").indexing(QVec([QSym("qty")]), brackets=True)).gt(200)
    print(res)
    assert '''sp[`qty]>200''' == str(res)

    res = QIndexable("sp").where(QOperable(QIndexable("sp").indexing(QVec([QSym("qty")]), brackets=True)).gt(200))
    print(res)
    assert '''sp where sp[`qty]>200''' == str(res)


def test13():
    res = QDictionary({"item": QSym("screw"), "qty": 500, "price": 1.95})
    print(res)
    assert '''`item`qty`price!(`screw;500;1.95)''' == str(res)

    q_assign("pr", QDictionary({"screw": 0.75, "nail": 3, "bolt": 2.85, "nut": 0.55}).single_row_vector()).test(
        '''pr:`screw`nail`bolt`nut!0.75 3 2.85 0.55''')

    res = QIndexable("pr").indexing(QVec([QSym("bolt"), QSym("nail")]), brackets=False)
    print(res)
    assert '''pr `bolt`nail''' == res

    res = QOperable("pr").gt(2)
    print(res)
    assert '''pr>2''' == str(res)


def test14():
    res = q_concat2("sp", QDictionary({"s": QSym("s5"), "p": QSym("p3"), "qty": 159}))
    print(str(res))
    assert '''sp,`s`p`qty!(`s5;`p3;159)''' == res


def test15():
    QFun("x*x").call(QVec([2, -1.5, 17])).test('''{x*x} 2 -1.5 17''')

    QFun(q_concat(
        [QStr("<"), "e", QStr(" "), "a", QStr(r"=\""), "v", QStr(r"\">"), "c", QStr("</"), "e",
         QStr(">")]), params=["e", "a", "v", "c"]).assign_to_name("el").test(
        r'''el:{[e;a;v;c]"<",e," ",a,"=\"",v,"\">",c,"</",e,">"}''')

    QFun(name="el", body="").call(
        QList([QStr("a"), QStr("href"), QStr("https://example.com/"), QStr("link text")]), brackets=True).test(
        r'''el["a";"href";"https://example.com/";"link text"]''')


def test16():
    res = QOperable(QVec([2, 3, 4]), space=True).add(10)
    print(res)
    assert '''2 3 4 + 10''' == str(res)

    res = QOperable(QVec([2, 3, 4]), space=True).add(QVec([10, 100, 1000]))
    print(res)
    assert '''2 3 4 + 10 100 1000''' == str(res)


def test17():
    QFun.named("count").foreach(QList([QStr("quick"), QStr("brown"), QStr("fox")], parentheses=True)).test(
        '''count each("quick";"brown";"fox")''')

    res = QFun.named(".h.htc").call(QList([QSym("p"), QStr("The quick brown fox")]), brackets=True)
    print(res)
    assert '''.h.htc[`p;"The quick brown fox"]''' == str(res)

    res = QFun(".h.htc[y;x]").fold(initial=QStr("The quick brown fox"),
                                   rest=QVec([QSym("p"), QSym("body"), QSym("html")]), intermediate_steps=False)
    print(res)
    assert '''"The quick brown fox" {.h.htc[y;x]}/ `p`body`html''' == str(res)

    accumulator = QFun.named("sum").call(QIndexable('x').tail(2))
    res = QFun(f"x,{accumulator}").do_n_times(8, QVec([1, 1]), intermediate_steps=True)
    print(res)
    assert r'''8 {x,sum -2#x}\1 1''' == str(res)
