package _2023_8_14.leetcode785;

import java.util.*;

class Solution {
    // 巩固 二部图，本题就是一个二部图的原理题
    /*
    回顾昨天的二部图定义，一个图中，其每一条边的两个点都必须一个在 U 集合，一个在 V 集合
    更进一步的定义是，不可以存在 奇数个节点组成的环，只允许存在 偶数个节点组成的环

    判定的方法采用：染色法
     */
    static int n;
    static int[] color; // 1 -> red  -1 -> green  0 -> no color

    static boolean dfs(int x, int[][] graph, int parent) {
        boolean cur = true;
        for (int v : graph[x]) {
            if (v == parent) continue;
            if (color[v] == 0) {
                color[v] = -color[x];
                cur &= dfs(v, graph, x);
            } else if (color[v] == color[x])
                return false;
        }
        return cur;
    }

    public boolean isBipartite(int[][] graph) {
        n = graph.length;
        color = new int[n];
        boolean res = true;
        for (int i = 0; i < n; i++) {
            if (color[i] == 0) {
                color[i] = 1;
                res &= dfs(i, graph, -1);
            }
        }
        return res;
    }
}

public class leetcode785 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.isBipartite(new int[][]{{1, 3}, {0, 2}, {1, 3}, {0, 2}}));
    }
}
