#!/bin/python3


def brackets(n):
    def gen(n, count_o, count_c, string):
        if count_o + count_c == 2*n:
            yield string
        if count_o < n:
            yield from gen(n, count_o+1, count_c, string + "(")
        if count_c < count_o:
            yield from gen(n, count_o, count_c+1, string + ")")
    yield from gen(n, 0, 0, '')


if __name__ == '__main__':
    n = int(input())
    for br in brackets(n):
        print(br)
