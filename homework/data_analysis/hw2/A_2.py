#!/bin/python3

import sys


def ackermann(m, n):
    ackermann.counter = 0
    return supp_func(m, n)


def supp_func(m, n):
    ackermann.counter += 1
    if(m == 0):
        return n + 1
    elif(m > 0 and n == 0):
        return supp_func(m-1, 1)
    elif(m > 0 and n > 0):
        return supp_func(m-1, supp_func(m, n-1))
