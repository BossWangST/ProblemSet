package _2023_8_15.leetcode743;

import java.util.*;

class pair {
    int dest;
    int weight;

    public pair(int d, int w) {
        dest = d;
        weight = w;
    }
}

class Solution {
    // 典型的 Dijkstra 题，想要最短的时间，就是由最短的里面【最长的时间】决定
    // 比如从 2 号节点开始，到 1 3 5 6 节点利用 Dijkstra 算出来需要 5 6 7 8 分钟的话
    // 而从 2 号到 4 号节点需要 10 分钟，那么全部走完的最短时间就是 10 分钟 --> 关键路径！！！
    public int networkDelayTime(int[][] times, int n, int k) {
        var g = new ArrayList<ArrayList<pair>>();
        for (int i = 0; i < n; i++) g.add(new ArrayList<>());
        for (int[] edge : times) {
            // g[1] = [2, 3] 表示 1 和 2 的边权重为 3
            g.get(edge[0] - 1).add(new pair(edge[1] - 1, edge[2]));
        }
        int[] dist = new int[n];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k - 1] = 0;
        PriorityQueue<pair> q = new PriorityQueue<>(Comparator.comparingInt(node -> node.weight));
        q.add(new pair(k - 1, 0));
        while (q.size() > 0) {
            pair cur = q.poll();
            for (pair p : g.get(cur.dest)) {
                if (dist[p.dest] > dist[cur.dest] + p.weight) {
                    dist[p.dest] = dist[cur.dest] + p.weight;
                    q.add(p);
                }
            }
        }
        int res = 0;
        for (int d : dist) {
            if (d == Integer.MAX_VALUE) return -1;
            res = Math.max(res, d);
        }
        return res;
    }
}

public class leetcode743 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.networkDelayTime(new int[][]{{2, 1, 1}, {2, 3, 1}, {3, 4, 1}}, 4, 2));
    }
}
