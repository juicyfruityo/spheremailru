#!/bin/python3
import functools


def once(func):
    @functools.wraps(func)
    def wrapper(*args, **argv):
        try:
            index = once.names.index(func.__name__)
        except:
            index = -1
        if(index == -1):
            once.result = func(*args, **argv)
            once.names.append(func.__name__)
        return once.result
    return wrapper
once.names = []
