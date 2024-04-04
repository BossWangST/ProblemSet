package _2023_8_17.leetcode1334;

import java.util.*;
import java.util.stream.IntStream;

class pair {
    int dest;
    int weight;

    public pair(int d, int w) {
        dest = d;
        weight = w;
    }
}

class Solution {
    // 依旧是 Dijkstra 找最短路径
    public int[] get_shortest(int x, ArrayList<ArrayList<pair>> g) {
        int[] dist = new int[g.size()];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[x] = 0;
        PriorityQueue<pair> q = new PriorityQueue<>(Comparator.comparingInt(node -> node.weight));
        q.add(new pair(x, 0));
        while (q.size() > 0) {
            pair cur = q.poll();
            for (pair p : g.get(cur.dest)) {
                // relaxation
                if (dist[p.dest] > dist[cur.dest] + p.weight) {
                    dist[p.dest] = dist[cur.dest] + p.weight;
                    q.add(p);
                }
            }
        }
        return dist;
    }

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        var g = new ArrayList<ArrayList<pair>>();
        for (int i = 0; i < n; i++) g.add(new ArrayList<>());
        for (int[] edge : edges) {
            g.get(edge[0]).add(new pair(edge[1], edge[2]));
            g.get(edge[1]).add(new pair(edge[0], edge[2]));
        }
        int[] neigh = new int[n];
        for (int i = 0; i < n; i++) {
            int[] cur = get_shortest(i, g);
            int cur_nei = -1; // 去除自己到自己
            for (int val : cur) if (val <= distanceThreshold) cur_nei++;
            neigh[i] = cur_nei;
        }
        int[] sorted = IntStream.range(0, n).boxed().sorted(Comparator.comparingInt(i -> neigh[i])).mapToInt(i -> i).toArray();
        for (int i = 1; i < n; i++) {
            if (neigh[sorted[i - 1]] < neigh[sorted[i]]) return sorted[i - 1];
        }
        return n - 1;
    }
}

public class leetcode1334 {
}
