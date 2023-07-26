package _2023_7_26.leetcode1019;

import java.util.*;

/*
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

class Solution {
    public int[] nextLargerNodes(ListNode head) {
        var nums = new ArrayList<Integer>();
        ListNode p = head;
        while (p != null) {
            nums.add(p.val);
            p = p.next;
        }
        int[] res = new int[nums.size()];
        Arrays.fill(res, 0);
        var s = new Stack<Integer>();
        p = head;
        int idx = 0;
        while (p != null) {
            if (s.empty()) {
                s.push(idx++);
                p = p.next;
                continue;
            }
            while (!s.empty() && p.val > nums.get(s.peek())) {
                res[s.pop()] = p.val;
            }
            s.push(idx++);
            p = p.next;
        }
        return res;
    }
}

public class leetcode1019 {
    public static void main(String[] args) {
        ListNode n1 = new ListNode(5);
        ListNode n2 = new ListNode(1, n1);
        ListNode root = new ListNode(2, n2);
        var s = new Solution();
        System.out.println(Arrays.toString(s.nextLargerNodes(root)));
    }
}
