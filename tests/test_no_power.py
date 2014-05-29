# -*- coding: utf-8 -*-
from no_powered import (power, powered_number, power_nono_number, gen,
                        no_power, prime, all_powered)

def test_get_powred():
    assert [4, 9] == list(power(10))


def test_powered_list():
    r = powered_number(20)
    for x in [4, 8, 9, 12, 16, 18]:
        assert x in r


def test_nono_number():
    assert 7 == power_nono_number(10)


def test_nono_tc_number():
    s = 1000000000L
    e = 1009999999L
    print list(power(s, e))
    assert list(power(s, e))


def test_gen():
    assert 4 == gen(0)


def test_prime():
    assert [1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0] == prime(10)


def test_all_power():
#     assert 4 in all_powered(10)
#     assert 8 in all_powered(10)
#     assert 9 in all_powered(10)
    print all_powered(1000000000L)
    assert False
