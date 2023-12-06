from lib0.QDate import QDate
from lib0.QDictionary import QTable
from lib0.QIterable import QIterable
from lib0.QList import QList
from lib0.QVector import QVector
from lib0.list_utils import *
from lib0.file_utils import *
from lib0.lang_utils import q_assign
from lib0.mem_utils import *
from lib0.QMinute import QMinute
from lib0.QString import QString
from lib0.QSymbol import QSymbol
from lib0.QTime import QTime
from lib0.trig_utils import *
from lib0.web_utils import q_download_csv
from lib0.sql_utils import *
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


# the-q-session
def test1():
    res = q_add(2, QVector([2, 3, 4]))
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
    url_expr = QString("https://code.kx.com/download/data/example.csv")
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

    res2 = q_update_from_where(q_assign("qty", q_mul("qty", 2)), "sp", q_logical_test_eq("p", QSymbol("p2")))
    print(res2)
    assert '''update qty:qty*2 from sp where p = `p2''' == res2


# language
def test8():
    res = q_mul(QVector([1, 2, 3]), q_acos(-1))
    print(res)
    assert '''1 2 3*acos -1''' == res

    res2 = QVector([QDate(datetime(2019, 7, 5)),
                    QDate(datetime(2019, 9, 15)),
                    QDate(datetime(2019, 11, 16)), ]).count()
    print(res2)
    assert '''count 2019.07.05 2019.09.15 2019.11.16''' == res2

    res3 = QVector([QMinute(time(hour=8, minute=30)),
                    QMinute(time(hour=12, minute=45)),
                    QMinute(time(hour=17, minute=15)), ]).count()
    print(res3)
    assert '''count 08:30 12:45 17:15''' == res3

    res4 = q_count(QVector([QTime(time(hour=22, minute=45, second=53, microsecond=600000)),
                            QTime(time(hour=22, minute=45, second=53, microsecond=601000)),
                            QTime(time(hour=22, minute=45, second=53, microsecond=602000)), ]))
    print(res4)
    assert '''count 22:45:53.600 22:45:53.601 22:45:53.602''' == res4

    res5 = q_count(QString("fox"))
    print(res5)
    assert '''count "fox"''' == res5

    res6 = q_count(QList([QString("quick"), QString("brown"), QString("fox")], enclose_parentheses=True))
    print(res6)
    assert '''count ("quick";"brown";"fox")''' == res6

    res7 = QList([QString("quick"), QString("brown"), QString("fox")], enclose_parentheses=True).foreach().count()
    print(res7)
    assert '''count each ("quick";"brown";"fox")''' == res7

    res8 = QVector([QSymbol("quick"), QSymbol("brown"), QSymbol("fox")]).count()
    print(res8)
    assert '''count `quick`brown`fox''' == res8

    res9 = QVector([QSymbol("quick"), QSymbol("brown"), QSymbol("fox")]).foreach().count()
    print(res9)
    assert '''count each `quick`brown`fox''' == res9


def test9():
    res = QList([42, QString("foxes"), QVector([QSymbol("screw"), QSymbol("bolt")]), QDate(datetime(2020, 9, 15))],enclose_parentheses=True).count()
    print(res)
    assert '''count (42;"foxes";`screw`bolt;2020.09.15)''' == res


def test10():
    res = QVector([3, 1, 4, 5]).count()
    print(res)
    assert '''count 3 1 4 5''' == res

    res = QVector([3, 1, 4, 5.9]).count()
    print(res)
    assert '''count 3 1 4 5.9''' == res

    res = q_count(QString("jump"))
    print(res)
    assert '''count "jump"''' == res

    res = q_logical_test_lt(QString("jump"), QString("n"))
    print(res)
    assert '''"jump" < "n"''' == res

    res = q_add(QDate(datetime(year=2020, month=1, day=1)), QVector([30, 60, 90, 120]))
    print(res)
    assert '''2020.01.01+30 60 90 120''' == res

    res = q_add(QMinute(time(hour=12)), QVector([30, 60, 90, 120]))
    print(res)
    assert '''12:00+30 60 90 120''' == res
