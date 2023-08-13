package _2023_8_13.leetcode886;

import java.util.*;

class Solution {
    static int[] color;

    static boolean dfs(int x, ArrayList<ArrayList<Integer>> g, int parent) {
        boolean cur = true;
        for (int v : g.get(x)) {
            if (v == parent) continue;
            if (color[v] != 0 && color[v] != color[x])
                continue;
            if (color[v] != 0 && color[v] == color[x])
                return false;
            color[v] = -color[x];
            cur &= dfs(v, g, x);
        }
        return cur;
    }

    public boolean possibleBipartition(int n, int[][] dislikes) {
        /*
        这是一道 二部图 的问题
        首先定义什么是 二部图：图中所有的边，其连接的 2 个节点必须在 2 个集合中，如果一条边连接的 2 个节点
        在同一个集合内，就寄
        也可以这样定义：一个图中只允许出现 长度为偶数的环，不允许出现 长度为奇数的环！

        那么这道题就非常明显，就是需要判定，这个 dislikes 给出的图，是不是一个二部图！
        如何判定？就是找 有没有长度为奇数的环！有就寄！

        怎么找？染色法！！！！老吉的书应该好好看啊！
        什么叫染色法？就是要遍历每一个节点，把其相邻的所有节点染成和自己不一样的颜色！如果已经有颜色的，就需要判定是不是和自己不一样
        如果是一样的，就完蛋！所以就是一个 DFS 或者 BFS 的过程！

         */
        var g = new ArrayList<ArrayList<Integer>>();
        color = new int[n];
        // 1 -> red  -1 -> green
        for (int i = 0; i < n; i++) g.add(new ArrayList<>());
        for (int[] edge : dislikes) {
            g.get(edge[0] - 1).add(edge[1] - 1);
            g.get(edge[1] - 1).add(edge[0] - 1);
        }
        boolean res = true;
        for (int i = 0; i < n; i++)
            if (color[i] == 0) {
                color[i] = 1;
                res &= dfs(i, g, -1);
            }
        return res;
    }
}

public class leetcode886 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.possibleBipartition(4, new int[][]{{1, 2}, {1, 3}, {2, 4}}));
    }
}
