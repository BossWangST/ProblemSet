package _2023_7_30.leetcode142;

import java.util.*;

/**
 * Definition for singly-linked list.
 */
class ListNode {
    int val;
    ListNode next;

    ListNode(int x) {
        val = x;
        next = null;
    }
}

class Solution {
    public ListNode detectCycle(ListNode head) {
        /*
        碰到这类链表题，首先想到双指针 slow 和 fast，今天这题很好的对双指针进行了研究
        假设这个链表节点数为 a + b，a 为【环外】的节点个数（不包含环的头），b 为【环内】的节点个数（包含环的头）
        那么考虑 141 题中判断链表中带环的方法：slow 和 fast 如果相遇则带环，否则没有环
        这道题在这里就需要对 slow 和 fast 的相遇进行分析，相遇的位置究竟在哪？
        1. 首先可以确定的是，相遇点必然在环内，不然不可能相遇
        2. 由于相遇必定是 fast【追上】slow，那么 fast 相比 slow，必然【多走了 n 个 b】！
        因为，每一回合，fast 和 slow 之间的距离都会增加 1，而进入环后，当且仅当 fast 和 slow 之间的距离 x % b == 0 时才会相遇
        所以 fast = 2 * slow 的同时还有一个等式：fast = slow + n * b
        最终，我们可以计算出，当 fast 和 slow 相遇的时候，其步数是确定的：
        fast = 2 * n * b
        slow = n * b
        回到问题上来：我们要找到环的开头，可以让一个指针（比如说 slow）走 k 步，保证 k = a + n * b 即可
        走 a 步就到了环的开头，后续如果要继续走，就必须走 b 步绕环一圈回到头
        现在注意到，这里的 k 中出现了一个好东西 n * b，也就是 fast 和 slow 相遇时 slow 走的步数
        如果在此时，让 slow 继续走 a 步，slow 所处的位置不就是环的开头了吗？
        那现在怎么确定环的开头，注意！有没有一个地方，走 a 步就到环的开头？有啊！不就是 head 吗？
        所以，找一个指针 p 从 head 开始走，和 slow 一样每次走 1 步，p 和 slow 相遇的时候必然就是环的开头！
         */
        ListNode slow = head, fast = head, p = head;
        if (head == null)
            return null;
        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
            if (slow == fast) {
                // 此时必然存在环
                while (p != slow) {
                    p = p.next;
                    slow = slow.next;
                }
                return p;
            }
        }
        return null;
    }
}

public class leetcode142 {
}
