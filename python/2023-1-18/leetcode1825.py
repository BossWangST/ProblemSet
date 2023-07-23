from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Node:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def insert(node: Node, val: int) -> Node:
    if node.val:
        if val < node.val:
            if node.left is None:
                node.left = Node(val)
            else:
                node.left = insert(node.left, val)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                node.right = insert(node.right, val)
    else:
        node.val = val
    return node


def delete(node: Node, val: int) -> Node:
    if node is None:
        return node
    if val < node.val:
        node.left = delete(node.left, val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        if node.left is None:
            temp = node.right
            node = None
            return temp
        elif node.right is None:
            temp = node.left
            node = None
            return temp

        # 找到右子树中最小的作为新的根
        temp = node.right
        while temp.left is not None:
            temp = temp.left
        node.val = temp.val
        node.right = delete(node.right, temp.val)

    return node


def Inorder(node: Node, cur: List[int]) -> List[int]:
    if node is None:
        return cur
    cur = Inorder(node.left, cur)
    cur.append(node.val)
    cur = Inorder(node.right, cur)
    return cur


class MKAverage:

    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.ori_arr = []
        self.arr = None
        self.size = 0
        # heapq.heapify(self.arr)

    def addElement(self, num: int) -> None:
        if self.arr is None:
            self.ori_arr.append(num)
            self.arr = Node(num)
            self.size += 1
        elif self.size >= self.m:
            cur = self.ori_arr.pop(0)
            self.arr = delete(self.arr, cur)
            self.ori_arr.append(num)
            self.arr = insert(self.arr, num)
        else:
            self.ori_arr.append(num)
            self.arr = insert(self.arr, num)
            self.size += 1
            # heapq.heappush(self.arr, num)

    def calculateMKAverage(self) -> int:
        if self.size < self.m:
            return -1
        res = Inorder(self.arr, [])
        return functools.reduce(lambda x, y: x + y, res[self.k:-self.k]) // (len(self.ori_arr) - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
obj = MKAverage(3, 1)
obj.addElement(3)
obj.addElement(1)
print(obj.calculateMKAverage())
obj.addElement(10)
print(obj.calculateMKAverage())
obj.addElement(5)
obj.addElement(5)
obj.addElement(5)
print(obj.calculateMKAverage())
