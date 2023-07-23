# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        p = [i for i in lists]
        head = ListNode()
        cur = head
        tail = cur

        def check(p: List[Optional[ListNode]]):
            i = 0
            while i < len(p):
                if p[i] is None:
                    p.remove(p[i])
                else:
                    i += 1
            return True if len(p) > 0 else False

        def get_next(cur: ListNode, p: List[Optional[ListNode]]):
            min_val = 10001
            min_head = -1
            for i in range(len(p)):
                if p[i].val < min_val:
                    min_val = p[i].val
                    min_head = i
            cur.val = min_val
            p[min_head] = p[min_head].next

        if not check(p):
            return None
        while check(p):
            cur.next = ListNode()
            get_next(cur, p)
            tail = cur
            cur = cur.next

        tail.next = None

        return head
