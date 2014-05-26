# -*- coding: utf-8 -*-

MAX = 1000000000000L

def gen(n):
    return n ** 2 + 4 * n + 4


def power(n, start=1):
    i = 0
    r = long(gen(i))
    while r < n:
        yield r
        i += 1
        r = long(gen(i))


def powered_number(until, start=1):
    n = []
    for num in power(until, start):
        i = 1
        r = num
        while r < until:
            if not r in n:
                n.append(r)
            i += 1
            r = i * num
    return n


def power_nono_number(end, start=1):
    powered = powered_number(start=start, until=end)
    return end - start - len(powered) + 1


if __name__ == '__main__':
    inputs = raw_input()
    s, e = inputs.split(' ')
    print '%d' % power_nono_number(start=long(s), end=long(e))
