# -*- coding: utf-8 -*-
from math import sqrt
from itertools import product


def prime(limit):
    """ Implement Sieve of Atkin
    """
    is_prime = [False for i in range(0, limit + 1)]
    sqrt_limit = int(sqrt(limit))
    ran = range(1, sqrt_limit + 1)
    for x, y in product(ran, ran):
        n = 4 * (x ** 2) + y ** 2
        if n <= limit and (n % 12 == 1 or n % 12 == 5):
            is_prime[n] = not is_prime[n]
        n = 3 * (x ** 2) + y ** 2
        if n <= limit and n % 12 == 7:
            is_prime[n] = not is_prime[n]
        n = 3 * (x ** 2) - y ** 2
        if x > y and n <= limit and n % 12 == 11:
            is_prime[n] = not is_prime[n]
    for n in range(5, sqrt_limit + 1):
        if is_prime[n]:
            k = n ** 2
            i = 1
            while k <= limit:
                is_prime[k] = False
                i += 1
                k = i * (n ** 2)
    is_prime[1] = True
    is_prime[2] = True
    is_prime[3] = True
    return is_prime


def num_of_nono_power(number):
    n = int(sqrt(number))
    prime(n)
