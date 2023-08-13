package _2023_8_13.leetcode1020;

import java.util.*;

class Solution {
    static boolean[][] vis;
    static int[][] dir;
    static int n, m;

    static int dfs(int x, int y, int[][] grid) {
        vis[x][y] = true;
        boolean cur = true;
        int child = 0;
        for (int[] d : dir) {
            int nx = x + d[0];
            int ny = y + d[1];
            if (0 > nx || nx >= n || 0 > ny || ny >= m) cur = false; // false 表示可以走出去
            if (0 <= nx && nx < n && 0 <= ny && ny < m && grid[nx][ny] == 1 && !vis[nx][ny]) {
                int c = dfs(nx, ny, grid);
                if (c == 0) cur = false;
                child += c;
            }
        }
        if (!cur) return 0;
        return 1 + child;
    }

    public int numEnclaves(int[][] grid) {
        n = grid.length;
        m = grid[0].length;
        // int[][] map = new int[n + 1][m + 1];
        dir = new int[][]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        vis = new boolean[n][m];
        /*
        for (int[] row : map) Arrays.fill(row, 2);
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++)
                map[i + 1][j + 1] = grid[i][j];
        */
        int res = 0;
        for (int i = 0; i < n; i++)
            for (int j = 0; j < m; j++) {
                if (!vis[i][j] && grid[i][j] == 1)
                    res += dfs(i, j, grid);
            }
        return res;
    }
}

public class leetcode1020 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.numEnclaves(new int[][]{{0, 0, 0, 0}, {1, 0, 1, 0}, {0, 1, 1, 0}, {0, 0, 0, 0}}));
    }
}
