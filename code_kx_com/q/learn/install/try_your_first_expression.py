from lib_q.mem_utils import q_exit_cli
from api.etc import range


def all_tests():
    test1()
    test2()


def test1():
    print(range(6))
    assert r"til 6" == str(range(6))


def test2():
    assert r"\\" == q_exit_cli()
