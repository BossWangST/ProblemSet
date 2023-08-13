package _2023_7_27.leetcode2500;

import java.util.*;

class Solution {
    public int deleteGreatestValue(int[][] grid) {
        var g = new ArrayList<ArrayList<Integer>>();
        for (int i = 0; i < grid.length; i++) {
            g.add(new ArrayList<>());
            for (int y : grid[i]) {
                g.get(i).add(y);
            }
            g.get(i).sort(Collections.reverseOrder());
        }
        int res = 0;
        int m;
        for (int j = 0; j < grid[0].length; j++) {
            m = -1;
            for (int i = 0; i < grid.length; i++)
                m = g.get(i).get(j) > m ? g.get(i).get(j) : m;
            res += m;
        }
        return res;
    }
}

public class leetcode2500 {
}
