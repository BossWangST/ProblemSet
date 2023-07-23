# Definition for singly-linked list.
from typing import List, Optional
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]], math=None) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        def merge_two(list1: Optional[ListNode], list2: Optional[ListNode]):
            dummy = ListNode()
            tail = dummy

            while list1 and list2:
                if list1.val < list2.val:
                    tail.next = list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                tail = tail.next
            if list1:
                tail.next = list1
            if list2:
                tail.next = list2
            return dummy.next

        while len(lists) > 1:
            next_list = []
            for j in range(0, len(lists), 2):
                l1 = lists[j]
                l2 = lists[j + 1] if j + 1 < len(lists) else None
                next_list.append(merge_two(l1, l2))
            lists = next_list

        return lists[0]
