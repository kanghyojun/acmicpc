# -*- coding: utf-8 -*-
from no_powered import power, powered_number, power_nono_number, gen, no_power

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
    assert [] == list(power(s, e))
    assert False


def test_gen():
    assert 4 == gen(0)


def test_new_way():
    assert 7 == no_power(1, 10)
