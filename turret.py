from math import sqrt

def turret(x0, y0, r0, x1, y1, r1):
    if x0 == x1 and y0 == y1:
        return -1
    interval = sqrt((x0 - x1) ** 2 + (y0 - y1) ** 2)
    r_interval = r0 + r1
    if interval > r_interval:
        r = 0
    elif interval == r_interval:
        r = 1
    elif interval < r_interval:
        r = 2
    return r


if __name__ == '__main__':
    count = int(raw_input())
    input_ = 5
    inputs = []
    i = 0
    while i < count:
        x = raw_input()
        inputs.append(x)
        i += 1
    for i in inputs:
        arg = [int(x) for x in i.split(' ')]
        print turret(*arg)
