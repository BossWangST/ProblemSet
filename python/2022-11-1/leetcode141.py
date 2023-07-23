# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        p = head
        while p is not None:
            if (p.val, p.next) not in visited:
                visited.add((p.val, p.next))
            else:
                return True
            p = p.next
        return False
