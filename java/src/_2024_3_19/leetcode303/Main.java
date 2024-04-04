package _2024_3_19.leetcode303;

import java.util.*;

class NumArray {
    public int[] nums;
    public int[] sum;

    public NumArray(int[] nums) {
        this.nums = nums;
        sum = new int[nums.length + 1];
        sum[0] = 0;
        for (int i = 0; i < nums.length; i++)
            sum[i + 1] = nums[i] + sum[i];
    }

    public int sumRange(int left, int right) {
        return sum[right + 1]  - sum[left];
    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */
public class Main {
    public static void main(String[] args) {
        var s = new NumArray(new int[]{-2, 0, 3, -5, 2, -1});
        System.out.println(s.sumRange(2, 5));
    }
}
