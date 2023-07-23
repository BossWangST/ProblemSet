from typing import List
import collections
import bisect


def sub_sort(left: int, right: int, nums: List) -> None:
    if left >= right:
        return
    pivot = nums[left]
    i, j = left, right
    while True:
        # i 找大的，j 找小的去交换
        while i < right and nums[i] <= pivot:
            i += 1
        while j > left and nums[j] > pivot:
            j -= 1

        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            break
    nums[left], nums[j] = nums[j], nums[left]
    sub_sort(left, j - 1, nums)
    sub_sort(i, right, nums)


def qsort(nums: List) -> None:
    sub_sort(0, len(nums) - 1, nums)


a = [1, 4, 5, 2, 3]
qsort(a)
print(a)
