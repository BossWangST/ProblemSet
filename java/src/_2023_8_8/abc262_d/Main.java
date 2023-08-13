package _2023_8_8.abc262_d;

import java.util.*;

public class Main {
    static int M = 998244353;
    static int[] fact;

    public static void initFact(int n) {
        fact = new int[n];
        fact[0] = 1;
        fact[1] = 1;
        for (int i = 2; i < n; i++)
            fact[i] = (i * fact[i - 1]) % M;
    }

    public static int nCk(int n, int k) {
        int up = fact[n] % M;
        int down = (fact[n - k] * fact[k]) % M;
        return (up / down) % M;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        initFact(n + 1);
        int[] nums = new int[n];
        for (int i = 0; i < n; i++) nums[i] = sc.nextInt();
        int res = n;
        for (int k = 2; k <= n; k++) {
            int cur = 0;
            for (int i = 0; i < n; i++) {
                if (nums[i] % k == 0)
                    cur = (cur + 1) % M;
            }
            if (cur >= k)
                res = (res + nCk(cur, k)) % M;
        }
        /*
        这个方法是错误的，应该使用 DP，留等后日再做
         */
        System.out.println(res);
    }
}
