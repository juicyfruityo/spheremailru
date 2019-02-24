#!/bin/python3
import functools
import time


def stopwatch(func):
    @functools.wraps(func)
    def wrapper():
        print("`%s` started" % func.__name__)
        start_time = time.time()
        result = func()
        fin_time = time.time() - start_time
        print("`%s` finished in %.2fs" % (func.__name__, fin_time))
        return result
    return wrapper
