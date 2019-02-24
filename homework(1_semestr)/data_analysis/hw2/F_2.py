#!/bin/python3
from operator import mul
from functools import reduce


def binomial(n):
    for k in range(-1, n):
        if k >= 0:
            C_k = C_k * (n - k) // (k + 1)
        else:
            C_k = 1
        yield str(int(C_k))


if __name__ == '__main__':
    for n in map(int, input().split()):
        print(' '.join(binomial(n)))
