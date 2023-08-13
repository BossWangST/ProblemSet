package _2023_8_9.leetcode1281;

import java.util.*;

class Solution {
    public int subtractProductAndSum(int n) {
        String s = Integer.toString(n);
        long p = 1;
        long sum = 0;
        for (int i = 0; i < s.length(); i++) {
            long p1 = Long.parseLong(s.substring(i, i + 1));
            p *= p1;
            sum += p1;
        }
        return (int) (p - sum);
    }
}

public class leetcode1281 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.subtractProductAndSum(234));
    }
}
