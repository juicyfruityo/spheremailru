from collections import deque


class BinarySearchTree:
    def __init__(self, value=None):
        self.left = self.right = None
        self.data = value

    def append(self, value):
        if self.data is None:
            self.data = value
        else:
            if self.data <= value:
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.append(value)
            else:
                if self.left is None:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.append(value)

    def __iter__(self):
        self.que = deque()
        self.que.append(self)
        return self

    def __next__(self):
        if len(self.que) == 0:
            raise StopIteration()
        x = self.que.popleft()
        if x.left is not None:
            self.que.append(x.left)
        if x.right is not None:
            self.que.append(x.right)
        if x.data is None:
            raise StopIteration()
        return x.data

    def __contains__(self, value):
        if self.data is None:
            return False
        elif self.data == value:
            return True
        elif self.data < value:
            if self.right is not None:
                return self.right.__contains__(value)
            else:
                return False
        else:
            if self.left is not None:
                return self.left.__contains__(value)
            else:
                return False
