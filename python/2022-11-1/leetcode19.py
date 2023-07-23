# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p = head
        l = list()
        while p is not None:
            l.append(p)
            p = p.next
        target = len(l) - n
        if target == 0:
            head = head.next
        elif target < len(l) - 1:
            l[target - 1].next = l[target + 1]
        else:
            l[target - 1].next = None

        return head
