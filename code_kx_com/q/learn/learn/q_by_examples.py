from lib_q.QFun import QFun, QOp
from lib_q.QList import QList
from lib_q.QOperable import QOperable
from lib_q.QStr import QStr
from lib_q.QVec import *
from lib_q.helper import asrt
from lib_q.lang_utils import q_parentheses, q_assign, q_brackets
from lib_q.list_utils import *
import api.etc as api


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


def test1():
    assert "2+2" == q_add(2, 2)
    assert "2-3" == q_subtract(2, 3)
    assert "2*3+4" == q_mul(2, q_add(3, 4))
    assert "3%4" == q_div(3, 4)
    assert "{x*x} 4" == str(QFun("x*x").call(4))
    assert "sqrt 4" == str(QFun.sqrt(4))
    assert "reciprocal 4" == str(QFun.reciprocal(4))


def test2():
    assert "2*1 2 3" == q_mul(2, QVec([1, 2, 3]))
    assert "1 2 3%2 4 6" == q_div(QVec([1, 2, 3]), QVec([2, 4, 6]))
    assert "count 1 2 3" == str(QFun.count(QVec([1, 2, 3])))
    assert "5#1 2" == api.rep([1, 2], 5)


def test3():
    assert "first 1 2 3" == str(QFun.first(QVec([1, 2, 3])))
    assert "last 1 2 3" == str(QFun.last(QVec([1, 2, 3])))
    assert "1_1 2 3" == q_cut(QVec(1), QVec([1, 2, 3]))
    assert "-1_1 2 3" == q_cut(QVec(-1), QVec([1, 2, 3]))
    assert "reverse 1 2 3" == str(QFun.reverse(QVec([1, 2, 3])))
    assert "iasc 2 1 6" == str(QFun.iasc(QVec([2, 1, 6])))
    assert "asc 2 1 6" == str(QFun.asc(QVec([2, 1, 6])))


def test4():
    assert "1 2 3,10 20" == q_concat([QVec([1, 2, 3]), QVec([10, 20])])
    assert "1+2+3" == q_add(1, q_add(2, 3))
    assert "sum 1 2 3" == str(QFun.sum(QVec([1, 2, 3])))
    assert "sums 1 2 3" == str(QFun.sums(QVec([1, 2, 3])))
    assert "1,(1+2),(1+2+3)" == q_concat([1, q_parentheses(q_add(1, 2)), q_parentheses(q_add(1, q_add(2, 3)))])
    assert "{1_x+prev x} til 5" == str(QFun(f"{q_add(q_cut(1, 'x'), QFun.prev('x'))}").call(QFun.til(5)))
    QFun.sum(QIterable(
        QFun(q_cut(q_parentheses(q_mul(2, QFun.til(QFun.ceiling(q_mul(0.5, QFun.count("x")))))), "x")).call(
            QVec([1, 2, 3, 4, 5])))).test("sum each{(2*til ceiling 0.5*count x)_x} 1 2 3 4 5")
    assert "(1 2;3 4 6;7 6)" == str(QList([QVec([1, 2]), QVec([3, 4, 6]), QVec([7, 6])], parentheses=True))
    assert "first (3 4 6;7 6)" == str(QFun.first(QList([QVec([3, 4, 6]), QVec([7, 6])], parentheses=True)))


def test5():
    assert "{x+x*x} 4" == str(QFun(q_add("x", q_mul("x", "x"))).call(4))
    QFun.compose([QFun.sqrt(), QFun(f"{q_mul('x', 'x')}")], multivariate=True).delcare_unary(4).test(
        "(sqrt;{x*x})@\: 4")
    assert "{x*x} sum 2 3" == str(QFun(q_mul("x", "x")).call(QFun.sum(QVec([2, 3]))))
    QFun.sum(QFun(q_mul("x", "x")).call(QVec([2, 3]))).test("sum {x*x} 2 3")
    QFun(QFun.sum(q_concat2(q_parentheses(q_mul("x", "x")), q_mul_fold(2, "x")))).call(
        QVec([2, 3])).test("{sum (x*x),2*/x} 2 3")
    assert "sqrt sum {x*x} 3 4" == str(QFun.sqrt(QFun.sum(QFun(q_mul("x", "x")).call(QVec([3, 4])))))


def test6():
    q_assign("d1", "-").test("d1:-")
    q_assign("d2", QFun("x-y")).test("d2:{x-y}")
    q_assign("m1", QFun.neg()).test("m1:neg")
    q_assign("m2", QFun.named("0-")).test("m2:0-")
    q_assign("m3", QFun("neg x")).test("m3:{neg x}")
    QFun.compose(["m1", "m2", "m3"], multivariate=True).delcare_unary(4).test(r"(m1;m2;m3)@\: 4")
    QFun.compose(["d1", "d2"], multivariate=True).delcare_binary(QVec([3, 4])).test(r"(d1;d2) .\: 3 4")


def test7():
    QList(["e", q_mul(2, "e"), q_mul("e", q_assign("e", QFun.exp(1)))], parentheses=True).test("(e;2*e;e*e:exp 1)")
    QFun.exp(2).test("exp 2")
    QFun.xexp(base=2, expo=16).test("2 xexp 16")
    QFun.log(QFun.exp(2)).test("log exp 2")
    QFun.xlog(base=2, number=65536).test("2 xlog 65536")


def test8():
    q_assign("a", QList(["pi", q_mul(2, "pi"), q_mul("pi", q_assign("pi", QFun.acos(-1)))], parentheses=True)).test(
        "a:(pi;2*pi;pi*pi:acos -1)")
    QFun.cos("pi").test("cos pi")

    q_assign("t", QFun.compose(
        [QFun.sum(), QFun(q_mul("x", "x")), QList([QFun.cos(), QFun.sin()], parentheses=True)]).delcare_unary()).test(
        "t:sum {x*x} (cos;sin)@\:")


def test9():
    api.outer_prod(QVec([1, 2, 3]), QVec([1, 2, 3])).test("1 2 3 */: 1 2 3")
    api.eye(3).test("{x =/: x} til 3")
    api.reshape(api.range(6), [2, 3]).test("2 3 # til 6")
    api.reshape(QVec([0, 1, 1, 1]), [2, 2]).test("2 2 # 0 1 1 1")

    QFun.show(q_assign("N", QOp.cut().map_right().call([QVec([0, 3]), api.reshape(api.range(12), [2, 6])]))).test(
        "show N:0 3 _/: 2 6 # til 12")
    QFun.raze().converge().call(q_brackets("N")).test("raze/ [N]")
    QFun.raze().foreach("N").test("raze each N")
    QFun.show(q_assign("M", QOp.take(QVec([3, 3]), QStr("ABC123!@#")))).test('show M:3 3 # "ABC123!@#"')
    QFun.compose([QOp.alias(), QFun.flip(), QFun.reverse(), QFun.reverse(QFun.each()), QFun.rotate(1)],
                 multivariate=True).delcare_unary("M").test('(::;flip;reverse;reverse each;1 rotate )@\: M')
    QFun.named("M").apply_binary().apply_unary(
        QFun.compose([QFun.named("f"), QFun.value(), QFun.group(), QFun.sum(),
                      QFun.each(q_assign("f", QFun.cross("n", q_assign("n", QFun.til(3)))))])).test(
        "M ./:/: f value group sum each f:n cross n:til 3")
    QFun.named("M").apply_binary(api.zip("a", q_assign("a", QFun.til(QFun.count("M"))))).test(
        "M ./: a ,' a:til count M")


def test10():
    q_assign("N", QList([QList([QVec([0, 1, 2]), QVec([3, 4, 5])], parentheses=True),
                         QList([QVec([6, 7, 8]), QVec([9, 10, 11])], parentheses=True)], parentheses=True)).test(
        "N:((0 1 2;3 4 5);(6 7 8;9 10 11))")
    assert """((N 1) 1) 1""" == (
        QIndexable(QIndexable(QIndexable(QIndexable("N").indexing(QVec([1]), brackets=False, outer_parenthesis=True)
                                         ).indexing(QVec([1]), brackets=False, outer_parenthesis=True))
                   ).indexing(QVec([1]), brackets=False))
    QFun.named(api.apply_n_times(3, QFun.named("@").call(QList(["", 1]), brackets=True))).call("N").test(
        '''3 @[;1]/  N''')
    assert """N[1;1;1]""" == QIndexable("N").indexing(indexes=QList([1, 1, 1]))
    QOp.dot("N", QVec([1, 1, 1])).test("N . 1 1 1")


def test11():
    # factorial and binomial
    QFun(q_assign("f", api.ternary(QOperable("x").lt(0), 0, QFun.prd(q_add("1.", QFun.til("x")))))).call(
        q_add(1, QFun.til(5))).print()
    QFun.prds(q_add(1, QFun.til(5))).test("prds 1+til 5")

    assert "15 mmu[M]/ M" == api.mpow_int("M", 15) + "M"


def test12():
    assert "-1 + 10?2.0" == api.runif(10, -1, 1.)
    asrt(api.rand_bool(10), "10?0b")
    asrt(api.sample(3, 3, replace=False), "-3?3")
    asrt(api.first_where(0, QVec([1, 2, 0, 3])), "1 2 0 3?0")
    asrt(api.monte_carlo_prob("1 0 2", random_sample=api.sample(3, 3, False, 1000)), "avg 1 0 2 ~/: 1_1000{-3?3}\()")


def test13():
    asrt(api.uniq(QStr("mississippi")), 'distinct "mississippi"')
    asrt(api.first_where("S", "D"), 'D?S')
    asrt(QList("S").indexing(api.values_of(api.keys_grouped_by_value("K")), brackets=False), "S value group K")
    asrt(QFun.count(QFun.each(QFun.group("S"))), "count each group S")
    asrt(QList("S").indexing(api.index_of_true("I"), brackets=False), "S where I")
    asrt(QFun.sum(QOp.eq("D", "S", ext="/:")), "sum D =/: S")
