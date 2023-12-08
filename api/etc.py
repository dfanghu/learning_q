from lib_q.QFun import QFun, QOp
from lib_q.QVec import QVec, QIndexable
from lib_q.lang_utils import q_vectorize_one_of_two_params
from lib_q.list_utils import q_add


def seq(n: int):
    return q_add(1, QFun.til(n))


def rep(x: list, length_out: int) -> str:
    return f"{length_out}#{' '.join([str(e) for e in x])}"


def range(n: int):
    return QFun.til(n)


def eye(n: int):
    return QFun(QOp.eq("x", "x", ext="/:")).call(QFun.til(n))


def reshape(x, shape: list):
    return QOp.take(QVec(shape), x)


def rotate_prev(lst, offset: int):
    return QFun.rotate(offset=offset, lst=lst)


def transpose(x):
    return QFun.flip(x)


def expand_grid(x, y):
    QFun.cross(x, y)


def group_by_value(lst):
    QFun.group(lst)


def zip(x, y):
    return QOp.comma(x, y, ext="'")


def apply_n_times(n, f: QFun):
    return f"{n} {f}/ "


def ternary(cond, iftrue, otherwise):
    return f"$[{cond};{iftrue};{otherwise}]"


def inner_prod(x, y):
    return QFun.wsum(x, y)


def mmult(x, y):
    return QFun.mmu(x, y)


def mpow_int(x, p: int):
    return q_vectorize_one_of_two_params("mmu", x, True, p)


def outer_prod(x, y):
    return QFun(name="*/:", argsin=[x, y], infix=True)


def runif(n: int, a: float, b: float):
    return f"{a} + {n}?{b - a}"


def rand_bool(n: int):
    return f"{n}?0b"


def sample(sample_size: int, population_size: int, replace: bool = False, repeat: int = 1):
    if not replace and sample_size > population_size:
        raise "sample size is greater than population size"
    res = f"{sample_size}?{population_size}"
    if not replace:
        res = "-" + res
    if repeat > 1:
        return f"1_{repeat}{{{res}}}\()"
    return res


def monte_carlo_prob(subject_point, random_sample):
    return QFun.avg(QOp.tilde(subject_point, random_sample, ext="/:"))


def first_where(value, container_iterable):
    return f"{container_iterable}?{value}"


def uniq(x):
    return f"distinct {x}"


def levels(x):
    return f"D:distinct S:{x};D?S"


def do(f: QFun, n_times: int, initial, intermediate_step=False):
    return f.do_n_times(n_times, initial, intermediate_step)


def index_of_true(predicate):
    return f"where {predicate}"


def sample_of_index_for_histogram(lst):
    return f"where {lst}"


def values_of(x):
    return QFun.value(x)


def keys_grouped_by_value(x):
    return QFun.group(x)

