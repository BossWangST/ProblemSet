package _2023_8_7.abc288_f;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    static int n, s;
    static String x;
    static long M = 998244353;

    /*
    public static long func() {
        int i = 1;
        StringBuilder sb = new StringBuilder();
        sb.append(x.charAt(0));
        long p = 1;
        int k = 1 << (n - 2);
        while (k > 0) {
            if ((s & k) > 0) {
                p *= Long.parseLong(sb.toString()) % M;
                sb.setLength(0);
                sb.append(x.charAt(i));
            } else sb.append(x.charAt(i));
            i++;
            k >>= 1;
        }
        return p * Long.parseLong(sb.toString()) % M;
    }
     */

    public static void main(String[] args) {
        var sc = new Scanner(System.in);
        n = sc.nextInt();
        x = sc.next();
        /*
        long target = 1L << (n - 1);
        long res = 0;
        while (s < target) {
            res += func();
            res %= M;
            s++;
        }
         */
        /*
        每当遇到 2^n 个情况的这类题，都需要想想 DP，对于数组的暴力切分，你考虑所有 2^n - 1 种情况肯定是完蛋的
        所以，怎么考虑 DP？
        从答案的角度考虑子问题，如果只有 1 个数字，那很明显答案就是 它自己
        从 3 234 这个案例考虑
        所以 dp[0] = x[0] = 2
        那么到 dp[1] 呢？现在有 2 位数，我们知道第一位数已经搞定了，重要的就是如何从 dp[0] 转移到 dp[1] 呢？
        要么是 2 * 3，要么是 23，所以 dp[1] = 2 * 3 + 23 = 29
        那么到 dp[2] 呢？
        我们观察答案：2 * 3 * 4 + 23 * 4 + 2 * 34 + 234
        首先一定有的，就是 x[0:2] 本身的数字，剩下来的和前面的 dp 有什么关系呢？
        观察 dp[1] = 2 * 3 + 23，而 dp[1] * 4 = 2 * 3 * 4 + 23 * 4
        dp[0] = 2，而 dp[0] * 34 = 2 * 34
        那么 dp[2] = 234 + dp[1] * 4 + dp[0] * 34
        假设我们现在的数字长度加长到 4 位：2345
        dp[3] 我们就可以大胆推断
        dp[3] = 2345 + dp[2] * 5 + dp[1] * 45 + dp[0] * 345
        来验证一下对不对：
        dp[3] = 2345 + 2 * 345 + 23 * 45 + 234 * 5 + 2 * 3 * 45 + 2 * 34 * 5 + 23 * 4 * 5 + 2 * 3 * 4 * 5
        dp[2] * 5 = 234 * 5 + 2 * 3 * 4 * 5 + 23 * 4 * 5 + 2 * 34 * 5
        dp[1] * 45 = 2 * 3 * 45 + 23 * 45
        dp[0] * 345 = 2 * 345
        非常正确！
        所以 dp[i + 1] = x[0:i + 1] + sum(dp[j] * x[j + 1:i + 1]) for all j < i
        但是，这样一来，转移的时间复杂度就是 O(n)，遍历 x 又是 O(n)，总的时间复杂度就是 O(n^2) 了，还是寄
        下面思考，如何优化转移
        观察一下 dp[i] 和 dp[i + 1]
        dp[i] = x[0:i] + sum(dp[j] * x[j + 1:i]) for all j < i
        dp[i + 1] = x[0:i + 1] + sum(dp[j] * x[j + 1:i + 1]) for all j < i
        x[0:i + 1] = x[0:i] * 10 + x[i + 1]
        x[j + 1:i + 1] = x[j + 1:i] * 10 + x[i + 1]
        下面的推导很关键，建议如果你再看到这里的时候还是拿出纸和笔写一下就知道了
        dp[i + 1] = x[0:i] * 10 + x[i + 1] + 10 * sum(dp[j] * x[j + 1:i]) for all j < i + x[i + 1] * sum(dp[j]) for all j < i
        所以 dp[i + 1] = dp[i] * 10 + x[i + 1] + x[i + 1] * sum(dp[j]) for all j < i
        最终，现在状态转移的时间复杂度降到了 O(1)，总的时间复杂度就是 O(n) 了
         */
        var dp = new ArrayList<Long>();
        dp.add(Long.parseLong(String.valueOf(x.charAt(0))));
        long s = dp.get(0);
        for (int i = 0; i < n - 1; i++) {
            long cur = Long.parseLong(String.valueOf(x.charAt(i + 1)));
            dp.add((dp.get(i) * 10 + cur + cur * s) % M);
            s += dp.get(i + 1) % M;
        }
        System.out.println(dp.get(n - 1));
    }
}
