package _2023_7_25.leetcode2208;

import java.math.BigDecimal;
import java.util.*;

class Solution {
    public int halveArray(int[] num) {
        var pq = new PriorityQueue<Double>(num.length, Collections.reverseOrder());
        double s = 0;
        for (int x : num) {
            pq.add((double) x);
            s += x;
        }
        s /= 2;
        int res = 0;
        while (s > 0) {
            double c = pq.poll();
            c /= 2;
            s -= c;
            pq.add(c);
            res++;
        }
        return res;
    }
}

public class leetcode2208 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.halveArray(new int[]{}));
    }
}
