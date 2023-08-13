package _2023_7_29.leetcode141;

import java.util.*;

class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null)
            return false;
        // 链表双指针的新玩法：快慢指针
        // 一个 fast 指针，一个 slow 指针，fast 每次走 2 步，slow 每次走 1 步
        ListNode fast = head, slow = head;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (fast == slow) {
                // 按理说，单向链表的快慢指针不可能相等，但是如果相等了则说明：快指针【追上了】慢指针
                // 也就是说，存在环！
                return true;
            }
        }
        return false;
    }
}

public class leetcode141 {
    public static void main(String[] args) {
        ListNode n1 = new ListNode(-4);
        ListNode n2 = new ListNode(0);
        ListNode n3 = new ListNode(2);
        ListNode n4 = new ListNode(3);
        n4.next = n3;
        n3.next = n2;
        n2.next = n1;
        n1.next = n3;
        var s = new Solution();
        System.out.println(Boolean.toString(s.hasCycle(n4)));
    }
}
