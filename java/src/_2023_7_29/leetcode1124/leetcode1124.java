package _2023_7_29.leetcode1124;

import java.util.*;

class Solution {
    public int longestWPI(int[] hours) {
        // 再一次的单调栈
        /*
        先考虑怎么转化题目，我们要找一个子数组，其【累】的个数大于【不累】的个数
        那么完全可以将【累】看作 1，【不累】看作 -1，如果一个子数组的和 > 0，那么其就是一个合法的答案
        子数组求和很明显就是前缀和
        现在的题目就转化成了：找 2 个下标 a < b，需要 s[b] - s[a] > 0 且 b - a 最大
        单独观察前缀和数组 s
        要想 b - a 尽可能大，则肯定找到越小的 s[a] 越好，因为这样可以让后续的 s[b] 要求降低
        如果我们将 s[a] 的递减序列存放在一个栈中，这些 s[a] 都是有成为真正的 a 的可能性的
        这里很关键的一步是：假如 s[a] 的序列是 8 4 6 5 3 2，为什么只需要记录 8 4 3 2 这个递减序列呢？
        因为，如果说将 5 作为子数组的左端点，而右端点找了个 9（9 > 5），那么很明显 5 之前的 4 作为左端点的子数组更长！！！！
        即如果在 s 数组前面已经有更小的了（比方说在遍历到 5 的时候，前面已经遍历过 4 了）那么【必然】当前的 s 值不能作为子数组的右端点
         */
        int n = hours.length;
        int[] s = new int[n + 1];
        Arrays.fill(s, 0);
        var st = new ArrayDeque<Integer>();
        st.push(0); // 栈里面记录下标
        for (int i = 1; i <= n; i++) {
            s[i] = s[i - 1] + (hours[i - 1] > 8 ? 1 : -1);
            if (s[i] < s[st.peek()])
                st.push(i);
        }
        int res = 0;
        // 我们为了找到最长的 b - a，则 b 从最后往前走
        // 倒序遍历的原理是：如果说当前的 i 作为右端点找到了一个合法答案（其左端点是 a），那么 i - 1 作为右端点且左端点为 a 的合法答案必然长度要小
        for (int i = n; i >= 0; i--) {
            while (!st.isEmpty() && s[st.peek()] < s[i]) {
                res = Math.max(res, i - st.pop());
            }
        }
        return res;
    }
}

public class leetcode1124 {
}
