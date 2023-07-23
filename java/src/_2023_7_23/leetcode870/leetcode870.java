package _2023_7_23.leetcode870;

import java.util.*;
import java.util.stream.IntStream;

class Solution {
    public int[] advantageCount(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        int n = nums1.length;
        int[] res = new int[n];
        // 获取一个 [0, n - 1] 的数组
        var ids = IntStream.range(0, n).boxed().toArray(Integer[]::new);
        // 根据 nums2[i] 来排序获得 nums2 数组排序后的数组下标
        Arrays.sort(ids, Comparator.comparingInt(i -> nums2[i]));
        /*
        田忌赛马，首先从 nums1 的最小的数字看起，如果比 nums2 的最小值大，那直接拿下
        如果比 nums2 的小，那就用来抵掉 nums2 的最大的
         */
        int left = 0, right = n - 1;
        for (int x : nums1) {
            res[x > nums2[ids[left]] ? ids[left++] : ids[right--]] = x;
        }
        return res;
    }
}

public class leetcode870 {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(Arrays.toString(s.advantageCount(new int[]{2, 7, 11, 15}, new int[]{1, 10, 4, 11})));
    }
}
