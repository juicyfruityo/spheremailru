#!/bin/python3
from collections import deque


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def binary_insert(root, node):
    if root == None:
        root = node
    else:
        if root.data <= node.data:
            if root.right == None:
                root.right = node
            else:
                binary_insert(root.right, node)
        else:
            if root.left == None:
                root.left = node
            else:
                binary_insert(root.left, node)


def get_items(root):
    items = []
    que = deque()
    que.append(root)
    while(len(que) != 0):
        x = que.popleft()
        items.append(x.data)
        if(x.left != None):
            que.append(x.left)
        if(x.right != None):
            que.append(x.right)
    return items


def search_value(root, value):
    if root.data == value:
        return True
    elif root.data < value:
        if root.right != None:
            return search_value(root.right, value)
        else:
            return False
    else:
        if root.left != None:
            return search_value(root.left, value)
        else:
            return False


class TreeIterator:
    def __init__(self, root_):
        self.items = get_items(root_)
        self.cursor = -1

    def __next__(self):
        if self.cursor + 1 >= len(self.items):
            raise StopIteration()
        self.cursor += 1
        return self.items[self.cursor]


class BinarySearchTree:
    def __init__(self, value=None):
        self.root = Node(value)

    def __iter__(self):
        return TreeIterator(self.root)

    def append(self, value):
        node = Node(value)
        if self.root.data == None:
            self.root.data = value
        else:
            binary_insert(self.root, node)

    def __contains__(self, value):
        return search_value(self.root, value)
