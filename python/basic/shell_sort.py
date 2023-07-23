from typing import *
from collections import *
from bisect import *
from functools import *
from math import *
from itertools import *
from heapq import *


def shell_sort(nums):
    gap = len(nums) // 2
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap //= 2
    return nums


a = [77, 62, 14, 9, 30, 21, 80, 25, 70, 55]
a = shell_sort(a)
for i in a:
    print(i)
