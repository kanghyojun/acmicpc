# -*- coding: utf-8 -*-
from array import array
from math import sqrt

MAX = 1000000000000L

def gen(n):
    return n ** 2 + 4 * n + 4


def all_powered(until):
    num = until
    for x in xrange(0, int(sqrt(until))):
        p = x ** 2 + 4 * x + 4
        num -= 1
#         for y in xrange(1, (until / p) + 1):
#             a.append(y * p)
    return num


def gen_until(n):
    i = 0
    r = gen(i)
    while r < n:
        i += 1
        r = gen(i)
        if r < n:
            yield r


def no_power(start, end):
    all = end - start + 1
    return all


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


def prime(n):
    from math import sqrt
    i = 2
    r = [1 for x in xrange(1, n + 2)]
    while i <= sqrt(n):
        if r[i] == 0:
            continue
        j = i + i
        while j <= n:
            r[j] = 0
            j += i
        i += 1
    return r


if __name__ == '__main__':
    inputs = raw_input()
    s, e = inputs.split(' ')
    print '%d' % power_nono_number(start=long(s), end=long(e))
