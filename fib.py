import sys


def fib_str(n):
    r00 = 1
    r01 = 0
    r10 = 0
    r11 = 1
    if n == 0:
        return r00, r01
    else:
        i = 0
        n -= 2
        while i <= n:
            t0 = r10
            t1 = r11
            r10 = r00 + r10
            r11 = r01 + r11
            r00 = t0
            r01 = t1
            i += 1
    return r10, r11


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
        print '%d %d' % fib_str(item)
