package _2024_4_4.leetcode1901;

import java.util.*;

class Solution {
    private int get_max(int[][] mat, int mid) {
        // find max value index in the col.mid
        int m = -1;
        int res = -1;
        for (int i = 0; i < mat.length; i++) {
            if (mat[i][mid] > m) {
                m = mat[i][mid];
                res = i;
            }
        }
        return res;
    }

    public int[] findPeakGrid(int[][] mat) {
        int n = mat.length;
        int m = mat[0].length;
        int left = 0, right = m - 1;
        int mid;
        int mid_col_max_i;
        // Here, the binary search is to find the column that contains PEAK value.
        while (left < right) {
            mid = (left + right) / 2;
            mid_col_max_i = get_max(mat, mid);
            if (mid < m - 1 && mat[mid_col_max_i][mid] < mat[mid_col_max_i][mid + 1]) // if the mid column is not max
                left = mid + 1; // max is in the right part
            else if (mid > 1 && mat[mid_col_max_i][mid] < mat[mid_col_max_i][mid - 1]) // if the mid column is less than left part, the max is in left part
                right = mid - 1;
            else
                return new int[]{mid_col_max_i, mid};
        }
        mid_col_max_i = get_max(mat, left); // the correct one is in the "left" column
        return new int[]{mid_col_max_i, left};
    }
}

public class Main {
}
