# -*- coding: utf-8 -*-
from math import sqrt

MAX = 1000000000000L


def power(end, start=1):
    i = start
    while i < end:
        if sqrt(i) % 1 == 0 and i > 1:
            yield i
        i += 1


def powered_number(end, start=1):
    n = []
    for num in power(end, start):
        i = 1
        r = num
        while r < end:
            if not r in n:
                n.append(r)
            i += 1
            r = i * num
    return n


def power_nono_number(end, start=1):
    powered = powered_number(start=start, end=end)
    return end - start - len(powered) + 1


if __name__ == '__main__':
    inputs = raw_input()
    s, e = inputs.split(' ')
    print '%d' % power_nono_number(start=long(s), end=long(e))
