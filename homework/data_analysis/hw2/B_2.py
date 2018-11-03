#!/bin/python3

import sys


def solution1(str):
    return [i*4 for i in str]


def solution2(str):
    return [(i+1) * s for i, s in enumerate(str)]


def solution3(iterator):
    return [x for x in iterator if x % 5 == 0 or x % 3 == 0]


def solution4(arr):
    return [i for arr_i in arr for i in arr_i]


def solution5(n):
    return [(a, b, c) for c in range(5, n+1)
            for b in range(1, c+1)
            for a in range(1, b+1)
            if a*a + b*b == c*c]


def solution6(tup):
    return [list(map(lambda x: x+i, tup[1])) for i in tup[0]]


def solution7(arr):
    return [list(arr_i[j] for arr_i in arr)
            for j, _ in enumerate(arr[0])]


def solution8(arr):
    return [list(map(int, arr_i.split(" "))) for arr_i in arr]


def solution9(iterator):
    return {chr(ord('a') + i): i*i for i in iterator}


def solution10(arr):
    return {s[0].upper() + s[1:].lower() for s in arr if len(s) > 3}


solutions = {
    'solution1': solution1,
    'solution2': solution2,
    'solution3': solution3,
    'solution4': solution4,
    'solution5': solution5,
    'solution6': solution6,
    'solution7': solution7,
    'solution8': solution8,
    'solution9': solution9,
    'solution10': solution10,
}
