package _2023_8_6.leetcode24;

import java.util.*;

class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) return head;
        ListNode odd = head, even = head.next;
        ListNode p = even.next, o = odd, e = even;
        boolean tick = true;
        while (p != null) {
            if (tick) {
                o.next = p;
                o = o.next;
            } else {
                e.next = p;
                e = e.next;
            }
            p = p.next;
            tick = !tick;
        }
        ListNode res = null;
        tick = true;
        o = odd;
        e = even;
        while (o != null && e != null) {
            if (res == null) {
                res = e;
                e = e.next;
                p = res;
                continue;
            }
            if (tick) {
                p.next = o;
                o = o.next;
                p = p.next;
            } else {
                p.next = e;
                e = e.next;
                p = p.next;
            }
            tick = !tick;
        }
        if (o != null) {
            p.next = o;
            p = p.next;
        }
        if (e != null) {
            p.next = e;
            p = p.next;
        }
        p.next = null;
        return res;
    }
}

public class leetcode24 {
    public static void main(String[] args) {
        ListNode n1 = new ListNode(4);
        ListNode n2 = new ListNode(3, n1);
        ListNode n3 = new ListNode(2, n2);
        ListNode n4 = new ListNode(1, n3);
        var s = new Solution();
        s.swapPairs(n4);
    }
}
