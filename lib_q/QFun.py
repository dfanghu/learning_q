from lib_q.QAmend import QAmend
from lib_q.QExpression import QExpression
from lib_q.QIterable import QIterable
from lib_q.QList import QList
from lib_q.QVec import QVec
from lib_q.lang_utils import q_assign


class QFun(QExpression):

    def __init__(self, body="", params: list = None, name: str = "", infix: bool = False, ext: str = "",
                 islist: bool = False, argsin="", brackets: bool = False):
        self.params = params
        self.body = body
        self.name = name
        self.infix = infix
        self.ext = ext
        self.islist = islist
        self.argsin = argsin
        self.brackets = brackets

    @staticmethod
    def anonymous(body, argv: list = None):
        return QFun(body=body, name="", params=argv)

    @staticmethod
    def named(name: str = "", infix: bool = False, ext: str = ""):
        return QFun(body="", name=name, params=None, infix=infix, ext=ext)

    def fullname(self):
        return f"{self.name}{self.ext}"

    def head(self):
        if self.name != "":
            return self.fullname()
        res = self.body
        if self.params is not None:
            res = f"[{QList(self.params, parentheses=False)}]{res}"
        if not self.islist:
            res = "{" + str(res) + "}"
        return f"{res}{self.ext}"

    def tail(self):
        return str(self.argsin)

    def joiner(self):
        # head = self.head()
        # if len(head) > 0 and head[-1] in r"}])?/\:@*#.$":
        #     return ""
        # tail = self.tail()
        # if len(tail) > 0 and tail[0] in r"([{?/\:@*#.$":
        #     return ""
        return " "

    def head_join_tail(self):
        head = self.head()
        if len(head) == 0:
            raise "missing head"
        if self.infix:
            sep1 = " "
            sep2 = " "
            return f"{self.argsin[0]}{sep1}{head}{sep2}{self.argsin[1]}"
        tail = self.tail()
        if self.brackets:
            return f"{head}[{tail}]"
        return f"{head}{self.joiner()}{tail}".strip()

    def __str__(self):
        tail = self.tail()
        if tail == "":
            return self.head()
        return self.head_join_tail()

    def assign_to_name(self, name) -> QAmend:
        return q_assign(name, str(self))

    def call(self, argsin, brackets: bool = False):
        self.argsin = argsin
        self.brackets = brackets
        return self

        # head = self.name + self.ext if self.name != "" else str(self)
        # return QCall(head=head, argsin=argsin, brackets=brackets, infix=self.infix)

    def foreach(self, iterable):
        return self.call(QIterable(iterable))

    def derived(self, ext: str):
        self.ext = ext
        return self

    def map_right(self):
        return self.derived("/:")

    def map_left(self):
        return self.derived("\:")

    def converge(self):
        return self.derived("/")

    def fold(self, initial, rest, intermediate_steps=False):
        if self.infix:
            raise "Not Implemented for infix"
        op = "\\" if intermediate_steps else "/"
        return f"{initial} {self}{op} {rest}"

    def scan(self, initial, rest):
        return self.fold(initial=initial, rest=rest, intermediate_steps=True)

    def over(self, initial, rest):
        return self.fold(initial=initial, rest=rest, intermediate_steps=False)

    def do_n_times(self, n, initial, intermediate_steps=False):
        op = "\\" if intermediate_steps else "/"
        return f"{n} {self}{op}{initial}"

    @staticmethod
    def compose(funs: list, multivariate: bool = False, argsin="", ext: str = ""):
        body = str(QList(funs, parentheses=True)) if multivariate else str(QVec(funs))
        f = QFun(body=body, islist=True, ext=ext, argsin=argsin)
        return f

    def specify_arity(self, ext: str, argsin=""):
        f = QFun(name=str(self), islist=self.islist, ext=ext, argsin=argsin)
        return f

    def delcare_unary(self, argsin=""):
        return self.specify_arity(r"@\:", argsin=argsin)

    def delcare_binary(self, argsin=""):
        return self.specify_arity(r" .\:", argsin=argsin)

    def apply_unary(self, argsin=""):
        return self.specify_arity(r"/:", argsin=argsin)

    def apply_binary(self, argsin=""):
        return self.specify_arity(r" ./:", argsin=argsin)

    @staticmethod
    def unary(name: str, x=""):
        f = QFun.named(name)
        if x == "":
            return f
        return f.call(x)

    @staticmethod
    def binary(name: str, x="", y="", ext="", infix: bool = False):
        f = QFun.named(name=name, infix=infix, ext=ext)
        if x == "":
            return f
        return f.call([x, y])

    @staticmethod
    def sqrt(x=""):
        return QFun.unary("sqrt", x)

    @staticmethod
    def reciprocal(x=""):
        return QFun.unary("reciprocal", x)

    @staticmethod
    def sum(x=""):
        return QFun.unary("sum", x)

    @staticmethod
    def sums(x=""):
        """cumsum"""
        return QFun.unary("sums", x)

    @staticmethod
    def prd(x=""):
        return QFun.unary("prd", x)

    @staticmethod
    def prds(x=""):
        """cumprod"""
        return QFun.unary("prds", x)

    @staticmethod
    def count(x=""):
        return QFun.unary("count", x)

    @staticmethod
    def first(x=""):
        return QFun.unary("first", x)

    @staticmethod
    def last(x=""):
        return QFun.unary("last", x)

    @staticmethod
    def reverse(x=""):
        return QFun.unary("reverse", x)

    @staticmethod
    def til(x=""):
        return QFun.unary("til", x)

    @staticmethod
    def show(x=""):
        return QFun.unary("show", x)

    @staticmethod
    def iasc(x=""):
        return QFun.unary("iasc", x)

    @staticmethod
    def asc(x=""):
        return QFun.unary("asc", x)

    @staticmethod
    def prev(x=""):
        return QFun.unary("prev", x)

    @staticmethod
    def ceiling(x=""):
        return QFun.unary("ceiling", x)

    @staticmethod
    def neg(x=""):
        return QFun.unary("neg", x)

    @staticmethod
    def exp(expo=""):
        return QFun.unary("exp", expo)

    @staticmethod
    def xexp(base="", expo=""):
        return QFun.binary("xexp", x=base, y=expo, infix=True)

    @staticmethod
    def log(x=""):
        return QFun.unary("log", x)

    @staticmethod
    def xlog(base="", number=""):
        return QFun.binary("xlog", x=base, y=number, infix=True)

    @staticmethod
    def acos(x=""):
        return QFun.unary("acos", x)

    @staticmethod
    def cos(x=""):
        return QFun.unary("cos", x)

    @staticmethod
    def sin(x=""):
        return QFun.unary("sin", x)

    @staticmethod
    def raze(lst=""):
        """collapse by concat"""
        return QFun.unary("raze", lst)

    @staticmethod
    def flip(mat=""):
        return QFun.unary("flip", mat)

    @staticmethod
    def each(lst=""):
        return QFun.unary("each", lst)

    @staticmethod
    def rotate(offset="", lst=""):
        return QFun.binary("rotate", x=offset, y=lst, infix=True)

    @staticmethod
    def cross(x="", y=""):
        return QFun.binary("cross", x=x, y=y, infix=True)

    @staticmethod
    def group(lst=""):
        return QFun.unary("group", lst)

    @staticmethod
    def value(lst=""):
        return QFun.unary("value", lst)

    @staticmethod
    def wsum(x="", y="", ext=""):
        return QOp.binary(name="wsum", x=x, y=y, ext=ext)

    @staticmethod
    def mmu(x="", y="", ext=""):
        return QOp.binary(name="mmu", x=x, y=y, ext=ext)

    @staticmethod
    def avg(x=""):
        return QFun.unary("avg", x)

    @staticmethod
    def distinct(x=""):
        return QFun.unary("distinct", x)

    @staticmethod
    def in_(x="", y="", ext=""):
        return QOp.binary(name="in", x=x, y=y, ext=ext)


class QOp:

    @staticmethod
    def binary(name: str, x="", y="", ext=""):
        f = QFun.named(name=name, infix=True, ext=ext)
        if x == "":
            return f
        return f.call([x, y])

    @staticmethod
    def eq(x="", y="", ext=""):
        return QOp.binary(name="=", x=x, y=y, ext=ext)

    @staticmethod
    def add(x="", y="", ext=""):
        return QOp.binary(name="+", x=x, y=y, ext=ext)

    @staticmethod
    def subtract(x="", y="", ext=""):
        return QOp.binary(name="-", x=x, y=y, ext=ext)

    @staticmethod
    def mul(x="", y="", ext=""):
        return QOp.binary(name="-", x=x, y=y, ext=ext)

    @staticmethod
    def div(x="", y="", ext=""):
        return QOp.binary(name="%", x=x, y=y, ext=ext)

    @staticmethod
    def take(x="", y="", ext=""):
        return QOp.binary(name="#", x=x, y=y, ext=ext)

    @staticmethod
    def cut(x="", y="", ext=""):
        return QOp.binary(name="_", x=x, y=y, ext=ext)

    @staticmethod
    def alias(x="", y="", ext=""):
        return QOp.binary(name="::", x=x, y=y, ext=ext)

    @staticmethod
    def dot(x="", y="", ext=""):
        return QOp.binary(name=".", x=x, y=y, ext=ext)

    @staticmethod
    def comma(x="", y="", ext=""):
        return QOp.binary(name=",", x=x, y=y, ext=ext)

    @staticmethod
    def tilde(x="", y="", ext=""):
        return QOp.binary(name="~", x=x, y=y, ext=ext)
