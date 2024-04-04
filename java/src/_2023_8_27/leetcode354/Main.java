package _2023_8_27.leetcode354;

import java.util.*;

class Solution {
    // LIS 问题变种，练习一下 LIS 吧，走一步，回头看看走过的路！
    public int maxEnvelopes(int[][] envelopes) {
        // 注意，宽度相等情况下，高度需要从高到低排，防止 [4, 5] -> [4, 6] 这样的情况出现！！
        Arrays.sort(envelopes, (node1, node2) -> node1[0] == node2[0] ? Integer.compare(node2[1], node1[1]) : Integer.compare(node1[0], node2[0]));
        int n = envelopes.length;
        int[] h = new int[n];
        for (int i = 0; i < n; i++) h[i] = envelopes[i][1];
        /*
        很遗憾，这道题用传统的 O(n^2) 是过不了的，需要使用二分查找的方法，利用纸牌游戏的思路
        int[] dp = new int[n];
        Arrays.fill(dp, 1); // dp[i] 为到 nums[i] 的 LIS 长度，原本都是一个数字，长度为 1
        int res = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (h[j] < h[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                    res = Math.max(res, dp[i]);
                }
            }
        }
        return res;

         */
        // 二分查找法的 LIS 算法
        int piles = 0;
        int[] top = new int[n];
        for (int i = 0; i < n; i++) {
            int poker = h[i];
            int left = 0, right = piles; // 从牌堆里寻找 [0, piles)，找的 target 是 poker 的左边界，即第一个比 poker 大的堆
            while (left < right) {
                int mid = left + (right - left) / 2;
                if (top[mid] == poker) {
                    right = mid; // 尽可能往左边找 [left, mid)
                } else if (top[mid] < poker) {
                    left = mid + 1;
                } else if (top[mid] > poker) {
                    right = mid;
                }
            }
            if (left == piles) // 找到头了没找到
                piles++;
            top[left] = poker;
        }
        return piles; // 堆的数量就是 LIS 的长度
    }
}

public class Main {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.maxEnvelopes(new int[][]{{4, 5}, {4, 6}, {6, 7}, {2, 3}, {1, 1}}));
    }
}
