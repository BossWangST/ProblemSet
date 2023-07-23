# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        l = list()
        p = head
        while p is not None:
            l.append(p)
            p = p.next

        order = []
        n = len(l) - 1
        if len(l) % 2 == 0:
            order_n = len(l) // 2
        else:
            order_n = len(l) // 2 + 1
        for i in range(order_n):
            order.append(i)
            order.append(n - i)
        for i in range(len(order) - 1):
            l[order[i]].next = l[order[i + 1]]
        l[order[len(order) - 1]].next = None
