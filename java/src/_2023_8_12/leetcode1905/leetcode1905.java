package _2023_8_12.leetcode1905;

import javax.xml.crypto.dsig.spec.XPathFilterParameterSpec;
import java.util.*;

class Solution {
    // 继续练习并查集 加入路径压缩
    static ArrayList<Integer> parent;
    static ArrayList<Integer> size;

    static int find(int x) {
        int root = x;
        while (parent.get(root) != root) root = parent.get(root);
        // path compression
        // 何为路径压缩？就是要让所有儿子直接指向祖宗！
        while (x != root) {
            int next = parent.get(x);
            parent.set(x, root); // 直接指向
            x = next;
        }
        return root;
    }

    static void union(int x, int y) {
        int x_parent = find(x);
        int y_parent = find(y);
        if (x_parent == y_parent) return;
        int x_size = size.get(x_parent);
        int y_size = size.get(y_parent);
        if (x_size < y_size) {
            parent.set(x_parent, y_parent);
            size.set(y_parent, x_size + y_size);
        } else {
            parent.set(y_parent, x_parent);
            size.set(x_parent, x_size + y_size);
        }
    }

    static boolean[][] vis;
    static int[][] dir;
    static int n, m;

    static void dfs(int x, int y, int root, int[][] grid) {
        vis[x][y] = true;
        union(x * m + y, root);
        for (int[] d : dir) {
            int nx = x + d[0];
            int ny = y + d[1];
            if (0 <= nx && nx < n && 0 <= ny && ny < m && !vis[nx][ny] && grid[nx][ny] == 1)
                dfs(nx, ny, root, grid);
        }
    }

    static boolean check_dfs(int x, int y, int root, int[][] grid) {
        vis[x][y] = true;
        boolean cur = find(x * m + y) == root;
        for (int[] d : dir) {
            int nx = x + d[0];
            int ny = y + d[1];
            if (0 <= nx && nx < n && 0 <= ny && ny < m && !vis[nx][ny] && grid[nx][ny] == 1)
                cur &= check_dfs(nx, ny, root, grid);
        }
        return cur;
    }

    public int countSubIslands(int[][] grid1, int[][] grid2) {
        parent = new ArrayList<>();
        size = new ArrayList<>();
        n = grid1.length;
        m = grid1[0].length;
        vis = new boolean[n][m];
        dir = new int[][]{{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        for (int i = 0; i < m * n; i++) {
            parent.add(i);
            size.add(1);
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!vis[i][j] && grid1[i][j] == 1)
                    dfs(i, j, i * m + j, grid1);
            }
        }
        vis = new boolean[n][m];
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (!vis[i][j] && grid1[i][j] == 1 && grid2[i][j] == 1 && check_dfs(i, j, find(i * m + j), grid2))
                    res++;
            }
        }
        return res;
    }
}

public class leetcode1905 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.countSubIslands(new int[][]{{1, 1, 1, 1, 0, 0}, {1, 1, 0, 1, 0, 0}, {1, 0, 0, 1, 1, 1}, {1, 1, 1, 0, 0, 1}, {1, 1, 1, 1, 1, 0}, {1, 0, 1, 0, 1, 0}, {0, 1, 1, 1, 0, 1}, {1, 0, 0, 0, 1, 1}, {1, 0, 0, 0, 1, 0}, {1, 1, 1, 1, 1, 0}}, new int[][]{{1, 1, 1, 1, 0, 1}, {0, 0, 1, 0, 1, 0}, {1, 1, 1, 1, 1, 1}, {0, 1, 1, 1, 1, 1}, {1, 1, 1, 0, 1, 0}, {0, 1, 1, 1, 1, 1}, {1, 1, 0, 1, 1, 1}, {1, 0, 0, 1, 0, 1}, {1, 1, 1, 1, 1, 1}, {1, 0, 0, 1, 0, 0}}));
    }
}
