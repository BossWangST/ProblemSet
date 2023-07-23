# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        p = head
        res = ListNode()
        res.val = p.val
        res.next = None
        p = p.next
        while p is not None:
            q = ListNode()
            q.next = res
            q.val = p.val
            res = q
            p = p.next
        return res
