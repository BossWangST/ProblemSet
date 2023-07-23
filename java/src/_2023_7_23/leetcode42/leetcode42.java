package _2023_7_23.leetcode42;

import java.util.*;

class Solution {
    public int trap(int[] height) {
        ArrayList<Integer> left_max = new ArrayList<Integer>();
        ArrayList<Integer> right_max = new ArrayList<Integer>();
        int m = 0;
        for (int i = 0; i < height.length; i++) {
            left_max.add(m);
            m = Math.max(m, height[i]);
        }
        m = 0;
        for (int i = height.length - 1; i >= 0; i--) {
            right_max.add(m);
            m = Math.max(m, height[i]);
        }
        Collections.reverse(right_max);
        int res = 0;
        for (int i = 0; i < height.length; i++) {
            res += Math.max(0, Math.min(left_max.get(i), right_max.get(i)) - height[i]);
        }
        return res;
    }
}

public class leetcode42 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.trap(new int[]{0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1}));
    }
}
