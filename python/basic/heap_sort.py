from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


def Heapify(idx: int, nums: List[int]) -> None:
    """
    :param idx: 需要进行 Heapify 的下标
    :param nums: 需要进行 Heapify 的数组
    :return: 已经 Heapify 好了的数组
    """
    if idx >= len(nums) // 2:
        return
    left, right = nums[idx * 2 + 1], nums[idx * 2 + 2] if idx * 2 + 2 < len(nums) else -inf
    # 找到最大的节点下标
    max_idx = idx
    if left > nums[max_idx]:
        max_idx = idx * 2 + 1
    if right > nums[max_idx]:
        max_idx = idx * 2 + 2
    if max_idx != idx:
        # 说明需要调整，记住调整后还需要继续向下递归调整
        nums[idx], nums[max_idx] = nums[max_idx], nums[idx]
        Heapify(max_idx, nums)
    return


def BuildHeap(nums: List[int]) -> List[int]:
    """
    :param nums: 无序数组，由此建堆
    :return: 建立好的堆
    """
    for i in range(len(nums) // 2, -1, -1):
        Heapify(i, nums)


def HeapSort(nums: List[int]) -> List[int]:
    res = []
    for i in range(len(nums)):
        BuildHeap(nums)
        res.append(nums.pop(0))
    return res


a = [5, 3, 1, 4, 2]
b = HeapSort(a)
for i in b:
    print(i)
