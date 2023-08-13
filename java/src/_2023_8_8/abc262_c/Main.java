package _2023_8_8.abc262_c;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[n];
        for (int i = 0; i < n; i++)
            nums[i] = sc.nextInt();
        int same = 0;
        long res = 0;
        for (int i = 0; i < n; i++) {
            if (nums[i] == i + 1) {
                same++;
            }
            else if (nums[i] > i + 1) {
                // 注意不要算重复了，前小后大 用 same 算，所以只要看 前大后小 的情况
                if (nums[nums[i] - 1] == i + 1)
                    res++;
            }
        }
        res += (long) same * (same - 1) / 2;
        System.out.println(res);
    }
}
