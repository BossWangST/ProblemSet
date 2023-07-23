package _2023_7_23.leetcode860;

import java.util.*;

class Solution {
    public boolean lemonadeChange(int[] bills) {
        var d = new HashMap<Integer, Integer>();
        d.put(5, 0);
        d.put(10, 0);
        d.put(20, 0);
        for (int x :
                bills) {
            d.put(x, d.get(x) + 1);
            if (x - 5 == 5) {
                d.put(5, d.get(5) - 1);
                if (d.get(5) < 0)
                    return false;
            } else if (x - 5 == 15) {
                if (d.get(5) > 0 && d.get(10) > 0) {
                    d.put(5, d.get(5) - 1);
                    d.put(10, d.get(10) - 1);
                } else if (d.get(5) > 2) {
                    d.put(5, d.get(5) - 3);
                } else
                    return false;
            }
        }
        return true;
    }
}

public class leetcode860 {

    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.lemonadeChange(new int[]{5, 5, 5, 10, 20}));
    }
}
