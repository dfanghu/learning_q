from lib.array_utils import q_range
from lib.mem_utils import q_exit_cli


def all_tests():
    test1()
    test2()


def test1():
    assert r"til 6" == q_range(6)


def test2():
    assert r"\\" == q_exit_cli()
