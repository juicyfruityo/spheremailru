#!/bin/python3
import operator
from operator import add
from functools import reduce


def solution1(arr):
    return [int(''.join(list(filter(str.isalnum, arr_i[::-1])))) for arr_i in arr]


def solution2(iterator):
    return [x[0]*x[1] for x in iterator]


def solution3(iterator):
    return [i for i in iterator
            if i % 6 == 0
            or i % 6 == 5
            or i % 6 == 2]


def solution4(arr):
    return [i for i in arr if bool(i) is True]


# переделать/доделать:
def solution5(rooms):
    for room in rooms:
        operator.setitem\
        (room, 'square', room['width'] * room['length'])
    return rooms


def solution6(rooms):
    return [i for i in solution5(rooms)]


def solution7(rooms):
    return [{'name': room['name'], 'width': room['width'],
            'length': room['length'], 'square': room['width']*room['length']}
            for room in rooms]
# ^^^^ надо бы переделать ^^^^


def solution8(people):
    return int(reduce(add, [man['height'] for man in people])), \
        len([man['height'] for man in people])


def solution9(students):
    return [stud['name'] for stud in students if stud['gpa'] > 4.5]


def solution10(tickets):
    return list(filter(lambda tick:
    sum(map(int, [x for i, x in enumerate(tick) if i % 2 == 0])) \
    == sum(map(int, [x for i, x in enumerate(tick) if i % 2 == 1])), tickets))

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
