# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2:
            return list1
        head = ListNode()
        p = list1
        q = list2
        cur = head
        tail = cur
        while p is not None and q is not None:
            cur.next = ListNode()
            if p.val < q.val:
                cur.val = p.val
                p = p.next
            else:
                cur.val = q.val
                q = q.next
            tail = cur
            cur = cur.next

        while p is not None:
            cur.next = ListNode()
            cur.val = p.val
            p = p.next
            tail = cur
            cur = cur.next
        while q is not None:
            cur.next = ListNode()
            cur.val = q.val
            q = q.next
            tail = cur
            cur = cur.next

        tail.next = None

        return head
