package _2023_7_31.leetcode143;

import java.util.*;

/**
 * Definition for singly-linked list.
 */
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

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        ListNode fast = head, slow = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }
        // slow 目前指向中点
        ListNode back = null;
        ListNode p = slow.next;
        ListNode q = p.next;
        slow.next = null;
        // 反转后半链表
        while (true) {
            p.next = back;
            back = p;
            p = q;
            if (q == null)
                break;
            q = q.next;
        }
        ListNode res = head;
        ListNode cur = res;
        p = head.next;
        q = back;
        boolean tick = true;
        while (p != null || q != null) {
            if (tick) {
                cur.next = q;
                q = q.next;
            } else {
                cur.next = p;
                p = p.next;
            }
            tick = !tick;
            cur = cur.next;
        }
        head = res;
    }
}
public class leetcode143 {
    public static void main(String[] args) {
        var s = new Solution();
        ListNode n4 = new ListNode(4);
        ListNode n3 = new ListNode(3, n4);
        ListNode n2 = new ListNode(2, n3);
        ListNode n1 = new ListNode(1, n2);
        s.reorderList(n1);
    }
}
