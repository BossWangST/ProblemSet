package _2023_8_15.leetcode1514;

import java.util.*;

class pair {
    int dest;
    double weight;

    public pair(int d, double w) {
        dest = d;
        weight = w;
    }
}

class Solution {
    // 今天复习 Dijkstra 算法，找“最短”路径
    /*
    核心是，每次从！！最近！！的点出发，看能不能缩短 start 到其他点的距离
     */
    public double maxProbability(int n, int[][] edges, double[] succProb, int start_node, int end_node) {
        var g = new ArrayList<ArrayList<pair>>();
        for (int i = 0; i < n; i++) g.add(new ArrayList<>());
        for (int i = 0; i < edges.length; i++) {
            g.get(edges[i][0]).add(new pair(edges[i][1], succProb[i]));
            g.get(edges[i][1]).add(new pair(edges[i][0], succProb[i]));
        }
        // init
        double[] dist = new double[n];
        dist[start_node] = 1; // self is always 100% possibility
        // BFS
        // 为了每次从【最大概率】的点出发去找，用最大堆
        PriorityQueue<pair> q = new PriorityQueue<>((node1, node2) -> node1.weight > node2.weight ? -1 : 1);
        q.add(new pair(start_node, 1));
        while (q.size() > 0) {
            pair cur_p = q.poll();
            int cur = cur_p.dest;
            double cur_w = cur_p.weight;
            if (dist[cur] > cur_w) continue; // 小小剪枝
            for (pair p : g.get(cur)) {
                // 每一个节点都把所有能够到的节点走一遍
                if (dist[p.dest] < dist[cur] * p.weight) {
                    dist[p.dest] = dist[cur] * p.weight; // relaxation
                    q.add(p);
                }
            }
        }
        return dist[end_node];
    }
}

public class leetcode1514 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.maxProbability(3, new int[][]{{0, 1}, {1, 2}, {0, 2}}, new double[]{0.5, 0.5, 0.2}, 0, 2));
    }
}
