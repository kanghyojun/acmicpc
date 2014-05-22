import sys


def fib_str(n):
    if n == 0:
        return 1, 0
    else:
        i = 0
        n -= 2
        f = (1, 0)
        s = (0, 1)
        while i <= n:
            t = s
            s = (f[0] + s[0], f[1] + s[1])
            f = t
            i += 1
        return s


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
