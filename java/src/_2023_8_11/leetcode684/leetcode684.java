package _2023_8_11.leetcode684;

import java.util.*;

class Solution {
    // 继续练习并查集
    static ArrayList<Integer> parent;
    static ArrayList<Integer> size;

    static int find(int x) {
        if (parent.get(x) == x) return x;
        return find(parent.get(x));
    }

    static void union(int x, int y) {
        int x_parent = find(x);
        int y_parent = find(y);
        if (x_parent == y_parent) return;
        int x_size = size.get(x_parent);
        int y_size = size.get(y_parent);
        if (x_size < y_size) {
            size.set(y_parent, x_size + y_size);
            parent.set(x_parent, y_parent);
        } else {
            size.set(x_parent, x_size + y_size);
            parent.set(y_parent, x_parent);
        }
    }

    public int[] findRedundantConnection(int[][] edges) {
        int n = edges.length;
        parent = new ArrayList<>();
        size = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            parent.add(i);
            size.add(1);
        }
        for (int[] edge : edges) {
            int u_parent = find(edge[0] - 1);
            int v_parent = find(edge[1] - 1);
            if (u_parent == v_parent) // 如果已经在一个集合里了，肯定出现环
                return edge;
            union(u_parent, v_parent);
        }
        return null;
    }
}

public class leetcode684 {
}
