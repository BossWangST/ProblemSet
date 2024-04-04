package _2023_8_16.leetcode1631;

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
    // 考虑将每个格子都看作是一个节点，两个相邻格子之间连带权的边，权重为 |diff|
    // 那么目标就是找到最“短”路径，这里的距离定义为路径中的 |diff| 最大值
    // 所以还是可以 Dijkstra 来
    public int minimumEffortPath(int[][] heights) {
        int n = heights.length;
        int m = heights[0].length;
        var g = new ArrayList<ArrayList<pair>>();
        for (int i = 0; i < n * m; i++) g.add(new ArrayList<>());
        // 注意，是无向边
        for (int i = 0; i < n - 1; i++) {
            g.get(i * m).add(new pair((i + 1) * m, Math.abs(heights[i][0] - heights[i + 1][0])));
            g.get((i + 1) * m).add(new pair(i * m, Math.abs(heights[i][0] - heights[i + 1][0])));
        }
        for (int i = 0; i < m - 1; i++) {
            g.get(i).add(new pair(i + 1, Math.abs(heights[0][i] - heights[0][i + 1])));
            g.get(i + 1).add(new pair(i, Math.abs(heights[0][i] - heights[0][i + 1])));
        }
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < m; j++) {
                g.get(i * m + j).add(new pair((i - 1) * m + j, Math.abs(heights[i][j] - heights[i - 1][j])));
                g.get((i - 1) * m + j).add(new pair(i * m + j, Math.abs(heights[i][j] - heights[i - 1][j])));
                g.get(i * m + j).add(new pair(i * m + j - 1, Math.abs(heights[i][j] - heights[i][j - 1])));
                g.get(i * m + j - 1).add(new pair(i * m + j, Math.abs(heights[i][j] - heights[i][j - 1])));
            }
        }
        int[] dist = new int[n * m];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[0] = 0;
        // 记得用自定义类的时候要给比较函数
        PriorityQueue<pair> q = new PriorityQueue<>(Comparator.comparingInt(node -> node.weight));
        q.add(new pair(0, 0));
        while (q.size() > 0) {
            pair cur = q.poll();
            for (pair p : g.get(cur.dest)) {
                if (dist[p.dest] > Math.max(dist[cur.dest], p.weight)) {
                    dist[p.dest] = Math.max(dist[cur.dest], p.weight);
                    q.add(p);
                }
            }
        }
        return dist[n * m - 1];
    }
}

public class leetcode1631 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.minimumEffortPath(new int[][]{{1, 2, 2}, {3, 8, 2}}));
    }
}
