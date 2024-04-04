package _2023_8_27.leetcode34;

import java.util.*;

class Solution {
    public int[] searchRange(int[] nums, int target) {
        if (nums.length == 0) return new int[]{-1, -1};
        if (nums.length == 1) {
            if (nums[0] == target) return new int[]{0, 0};
            else return new int[]{-1, -1};
        }
        // 练习二分写法，注意【区间】开闭！
        int left = 0, right = nums.length;
        int mid;
        while (left < right) { // [left, right) right是取不到的开区间
            // 还有一个注意点，保证 mid 不会被重复放在区间内
            mid = left + (right - left) / 2; // 防止溢出
            if (nums[mid] == target) {
                // 找最左的 target，在 mid 左侧找一找，由于要一直保持左闭右开区间，所以是 [left, mid)，则 right 必然是 mid
                right = mid;
            } else if (nums[mid] < target) {
                // 在 mid 右侧区间搜索，[mid + 1, right)
                left = mid + 1;
            } else if (nums[mid] > target) {
                // 在 mid 左侧区间搜索，[left, mid)
                right = mid;
            }
        }
        // 出来时，必然是 left == right, 对于区间而言就是 [left, left)，区间为空
        int l_max;
        if (left < 0 || left >= nums.length) l_max = -1;
        else
            l_max = nums[left] == target ? left : -1;

        left = 0;
        right = nums.length;
        while (left < right) {
            mid = left + (right - left) / 2;
            if (nums[mid] == target) {
                // 找最右边的 target，在 mid 右侧找，[mid + 1, right)
                left = mid + 1; // 由于最终 left 必然是（如果有 target 的话）mid + 1，所以最终的结果就是 left - 1
            } else if (nums[mid] < target) {
                // 去 mid 右侧找，[mid + 1, right)
                left = mid + 1;
            } else if (nums[mid] > target) {
                // 去 mid 左侧找，[left, mid)
                right = mid;
            }
        }
        int r_max;
        if (left - 1 < 0 || left - 1 >= nums.length) r_max = -1;
        else
            r_max = nums[left - 1] == target ? left - 1 : -1;
        return new int[]{l_max, r_max};
    }
}

public class Main {
}
