#!/bin/python3
from copy import deepcopy


class FragileDict:

    def __init__(self, dict=None):
        if dict is not None:
            self._data = deepcopy(dict)
        self._lock = True

    def __contains__(self, key):
        for d in self._data:
            if d == key:
                return True
        return False

    def __getitem__(self, key):
        if not self.__contains__(key):
            raise KeyError(key)
        return self._data[key]

    def __enter__(self):
        self.old_dict = deepcopy(self._data)
        self._lock = False

    def __exit__(self, exp_type, exp_value, exp_ptr):
        self._lock = True
        if exp_type:
            self._data = deepcopy(self.old_dict)
            del self.old_dict
            print("Exception has been suppressed.")
            return True
        del self.old_dict
        self._data = deepcopy(self._data)

    def __setitem__(self, key, value):
        if not self._lock:
            self._data[key] = value
        else:
            raise RuntimeError("Protected state")
