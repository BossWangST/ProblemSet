package _2023_8_4.leetcode980;

import java.util.*;

class Solution {
    public int[][] dir = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

    public int dfs(int[][] grid, ArrayList<ArrayList<Boolean>> vis, int x, int y) {
        if (grid[x][y] == 2) {
            vis.get(x).set(y, true);
            boolean res = true;
            for (List<Boolean> l : vis)
                res = res && l.stream().reduce(true, Boolean::logicalAnd);
            vis.get(x).set(y, false);
            if (res) return 1;
            else return 0;
        }
        vis.get(x).set(y, true);
        int cur = 0;
        for (int[] s : dir) {
            int nx = s[0] + x, ny = s[1] + y;
            if (0 <= nx && nx < grid.length && 0 <= ny && ny < grid[0].length && grid[nx][ny] != -1 && !vis.get(nx).get(ny))
                cur += dfs(grid, vis, nx, ny);
        }
        vis.get(x).set(y, false);
        return cur;
    }

    public int uniquePathsIII(int[][] grid) {
        var vis = new ArrayList<ArrayList<Boolean>>();
        int startX = 0, startY = 0;
        for (int i = 0; i < grid.length; i++) {
            vis.add(new ArrayList<>());
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == -1)
                    vis.get(i).add(true);
                else if (grid[i][j] == 1) {
                    startX = i;
                    startY = j;
                    vis.get(i).add(false);
                } else vis.get(i).add(false);
            }
        }
        return dfs(grid, vis, startX, startY);
    }
}

public class leetcode980 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.uniquePathsIII(new int[][]{{0, 0, 0, 0, 0, 0, 2, 0, 0, 0}, {0, 0, 0, 0, 0, 0, 0, 0, 1, 0}}));
    }
}
