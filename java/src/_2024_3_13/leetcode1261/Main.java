package _2024_3_13.leetcode1261;

import java.util.*;

/**
 * Definition for a binary tree node.
 */
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

class FindElements {
    public TreeNode root;
    public Set<Integer> s;

    public void dfs(TreeNode node) {
        if (node.left != null) {
            node.left.val = node.val * 2 + 1;
            s.add(node.left.val);
            dfs(node.left);
        }
        if (node.right != null) {
            node.right.val = node.val * 2 + 2;
            s.add(node.right.val);
            dfs(node.right);
        }
    }

    public FindElements(TreeNode root) {
        root.val = 0;
        s = new HashSet<>();
        s.add(0);
        dfs(root);
        this.root = root;
    }

    public boolean find(int target) {
        return s.contains(target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * FindElements obj = new FindElements(root);
 * boolean param_1 = obj.find(target);
 */
public class Main {
    public static void main(String[] args) {
    }
}
