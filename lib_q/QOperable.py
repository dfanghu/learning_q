from lib_q.QExpression import QExpression
from lib_q.QPredicate import QPredicate
from lib_q.list_utils import *


class QOperable(QExpression):

    def __init__(self, x, space: bool = False):
        self.x = x
        self.space = space

    def __str__(self):
        return str(self.x)

    def gt(self, rhs) -> QPredicate:
        return QPredicate(q_logical_test_gt(self, rhs, self.space))

    def ge(self, rhs) -> QPredicate:
        return QPredicate(q_logical_test_ge(self, rhs, self.space))

    def eq(self, rhs) -> QPredicate:
        return QPredicate(q_logical_test_eq(self, rhs, self.space))

    def neq(self, rhs) -> QPredicate:
        return QPredicate(q_logical_test_neq(self, rhs, self.space))

    def lt(self, rhs) -> QPredicate:
        return QPredicate(q_logical_test_lt(self, rhs, self.space))

    def le(self, rhs) -> QPredicate:
        return QPredicate(q_logical_test_le(self, rhs, self.space))

    def add(self, rhs):
        return q_add(self, rhs, self.space)

    def subtract(self, rhs):
        return q_subtract(self, rhs, self.space)

    def mul(self, rhs):
        return q_mul(self, rhs, self.space)

    def div(self, rhs):
        return q_div(self, rhs, self.space)
