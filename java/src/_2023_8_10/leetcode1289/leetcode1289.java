package _2023_8_10.leetcode1289;

import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int minFallingPathSum(int[][] grid) {
        int n, m;
        n = grid.length;
        m = grid[0].length;
        int[][] dp = new int[n][m];
        System.arraycopy(grid[0], 0, dp[0], 0, m);
        for (int i = 1; i < n; i++) {
            int finalI = i;
            int[] last = IntStream.range(0, m).boxed().sorted(Comparator.comparingInt(a -> dp[finalI - 1][a])).mapToInt(ele -> ele).toArray();
            for (int j = 0; j < m; j++) {
                int k = 0;
                for (; k < m; k++)
                    if (last[k] != j) break;
                dp[i][j] = dp[i - 1][last[k]] + grid[i][j];
            }
        }
        int res = Integer.MAX_VALUE;
        for (int i = 0; i < m; i++)
            res = Math.min(res, dp[n - 1][i]);
        return res;
    }
}

public class leetcode1289 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.minFallingPathSum(new int[][]{{2, 2, 1, 2, 2}, {2, 2, 1, 2, 2}, {2, 2, 1, 2, 2}, {2, 2, 1, 2, 2}, {2, 2, 1, 2, 2}}));
    }
}
