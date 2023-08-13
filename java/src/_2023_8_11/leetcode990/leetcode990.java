package _2023_8_11.leetcode990;

import java.util.*;

class Solution {

    static ArrayList<Integer> parent;
    static ArrayList<Integer> size;

    public static int find(int x) {
        if (parent.get(x) == x) return x;
        else return find(parent.get(x));
    }

    public static void union(int x, int y) {
        int x_parent = find(x);
        int y_parent = find(y);
        if (x_parent == y_parent) return;
        // 小的并入大的
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

    public boolean equationsPossible(String[] equations) {
        // 今天来练习并查集 Union Find
        // 我想总体思路很简单，如果等式左右两侧是同一个集合里的，结果是 != 就寄
        parent = new ArrayList<>();
        size = new ArrayList<>();
        for (int i = 0; i < 26; i++) {
            parent.add(i);
            size.add(1);
        }
        for (String s : equations) {
            int x, y;
            x = s.charAt(0) - 'a';
            y = s.charAt(3) - 'a';
            if (s.contains("==")) union(x, y);
        }
        for (String s : equations) {
            int x, y;
            x = s.charAt(0) - 'a';
            y = s.charAt(3) - 'a';
            if (s.contains("!=") && find(x) == find(y)) return false;
        }

        return true;
    }
}

public class leetcode990 {
}
