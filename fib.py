import sys


def fib_str(n):
    f = '0'
    s = '1'
    if n == 0:
        return f
    else:
        i = 0
        n -= 2
        while i <= n:
            t = s + f
            f = s
            s = t
            i += 1
        return s


def fib_counter(n):
    s = fib_str(n)
    r0 = 0
    for x in s:
        if x == '0':
            r0 += 1
    return r0, len(s) - r0


if __name__ == '__main__':
    count = int(raw_input())
    input_ = 5
    inputs = []
    i = 0
    while i < count:
        x = int(input())
        inputs.append(x)
        i += 1
    for item in inputs:
        print '%d %d' % fib_counter(item)
