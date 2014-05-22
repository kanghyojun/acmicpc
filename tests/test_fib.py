from fib import fib_str


def test_fib_str():
    assert (1, 0) == fib_str(0)
    assert (0, 1) == fib_str(1)
    assert (1, 1) == fib_str(2)
    assert (1, 2) == fib_str(3)
