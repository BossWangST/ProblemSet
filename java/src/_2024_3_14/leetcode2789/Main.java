package _2024_3_14.leetcode2789;

import java.util.*;

class Solution {
    public long maxArrayValue(int[] nums) {
        int n = nums.length;
        int i = n - 2, j = n - 1;
        if (n == 1)
            return nums[0];
        // basic idea is to calculate from last to first
        // This ensures that the larger num is definitely at the back part
        long l_nums[] = new long[n];
        for (int k = 0; k < n; k++) l_nums[k] = nums[k];
        while (i >= 0) {
            if (l_nums[i] <= l_nums[j]) {
                l_nums[i] += l_nums[j];
            }
            i--;
            j--;
        }
        return l_nums[0];
    }
}

public class Main {
}
