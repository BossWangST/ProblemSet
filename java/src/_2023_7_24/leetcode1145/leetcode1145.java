package _2023_7_24.leetcode1145;

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public void dfs(TreeNode node, ArrayList<Integer>[] g) {
        System.out.println("Current node:" + Integer.toString(node.val));
        if (node.left != null) {
            g[node.val].add(node.left.val);
            g[node.left.val].add(node.val);
            dfs(node.left, g);
        }
        if (node.right != null) {
            g[node.val].add(node.right.val);
            g[node.right.val].add(node.val);
            dfs(node.right, g);
        }
    }

    public int get_s(int node, ArrayList<Integer>[] g, int parent) {
        int cur = 0;
        for (int x : g[node]) {
            if (x != parent)
                cur += get_s(x, g, node);
        }
        return 1 + cur;
    }

    // left, right 是 x 节点的左子树大小和右子树大小，那么 x 父节点那棵树怎么办？n - left - right - 1 即可！
    private int x, left, right;

    public int dfs(TreeNode node) {
        int l = 0, r = 0;
        if (node.left != null)
            l += dfs(node.left);
        if (node.right != null)
            r += dfs(node.right);
        if (node.val == this.x) {
            this.left = l;
            this.right = r;
        }
        return l + r + 1;
    }
    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        /*
        ArrayList<Integer>[] g = new ArrayList[n + 1];
        Arrays.setAll(g, p -> new ArrayList<Integer>());
        dfs(root, g);
        var sub = new ArrayList<Integer>();
        int s = 0;
        for (Integer i : g[x]){
            sub.add(get_s(i, g, x));
            s += sub.get(sub.size() - 1);
        }
        for (int i : sub) {
            if (i > s - i)
                return true;
        }
        return false;

        */
        this.x = x;
        dfs(root);
        int s = n - 1;
        int parent = n - 1 - this.left - this.right;
        if (this.left > s - this.left || this.right > s - this.right || parent > s - parent)
            return true;
        return false;
    }
}

public class leetcode1145 {
    public static void main(String[] args) {
        var s = new Solution();

        System.out.println(Boolean.toString(s.btreeGameWinningMove(null, 10, 3)));
    }
}
