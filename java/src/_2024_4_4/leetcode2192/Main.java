package _2024_4_4.leetcode2192;

import java.util.*;

class Solution {
    ArrayList<Integer>[] g;
    List<Integer>[] res;
    int[] vis;

    private void dfs(int ancestor, int node) {
        vis[node] = ancestor; // 避免重复访问，vis所记录的是当前轮次的祖先
        for (int next :
                g[node]) {
            if (vis[next] != ancestor) { // next在当前这轮没走过，注意这里vis用int是为了记录每一轮不同的vis情况，比如第0轮vis=0就是访问过了，但是第一轮vis=1才是访问过
                // 这样就能保证每一轮中不会出现重复
                res[next].add(ancestor);
                dfs(ancestor, next);
            }
        }
    }

    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        this.vis = new int[n];
        Arrays.fill(vis, -1);
        this.g = new ArrayList[n];
        Arrays.setAll(g, i -> new ArrayList<>());
        this.res = new ArrayList[n];
        Arrays.setAll(res, i -> new ArrayList<>());
        for (int[] edge :
                edges) {
            g[edge[0]].add(edge[1]);
        }
        for (int i = 0; i < n; i++) {
            dfs(i, i);
        }
        return Arrays.asList(res);
    }
}

public class Main {
    public static void main(String[] args) {
        var s = new Solution();
        s.getAncestors(8, new int[][]{{0, 3}, {0, 4}, {1, 3}, {2, 4}, {2, 7}, {3, 5}, {3, 6}, {3, 7}, {4, 6}});
    }
}
