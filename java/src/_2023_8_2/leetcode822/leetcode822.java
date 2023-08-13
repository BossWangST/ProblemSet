package _2023_8_2.leetcode822;

import java.util.*;

class Solution {
    public int flipgame(int[] fronts, int[] backs) {
        var s = new HashSet<Integer>();
        for (int i = 0; i < fronts.length; i++) {
            if (fronts[i] == backs[i]) {
                s.add(fronts[i]);
            }
        }
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < fronts.length; i++) {
            if (!s.contains(fronts[i]))
                res = Math.min(res, fronts[i]);
            if (!s.contains(backs[i]))
                res = Math.min(res, backs[i]);
        }
        if (res == Integer.MAX_VALUE)
            return 0;
        return res;
    }
}

public class leetcode822 {
}
