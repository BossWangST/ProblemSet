package _2024_3_28.leetcode1997;

import java.util.*;

class Solution {
    public int firstDayBeenInAllRooms(int[] nextVisit) {
        // 由于 nextVisit[i] <= i，所以访问到 i 时，必然是从 (i + 1) % n 这个渠道来的，也就表示 i 左侧所有房间必然都被访问过了【偶数】次
        // 所以对于 房间 i，其访问次数会有 2 种状态：偶数（包括没访问时）和奇数（第一次访问时和之后的情况）
        // 我们定义 dp[i] 为“从访问到 i 且为奇数次，到访问到 i 且为偶数次”所需要的时间，也就是一整次【回访】的天数
        // 所以状态转移方程就是：dp[i] = sum(dp[nextVisit[i]], dp[i - 1]) + 2，这里前面的和是 [nextVisit[i], i-1] 回访总和，而 2 是对于房间 i 的2次访问（首次+ 回访1次）
        // 用前缀和优化一下，s[i + 1] = s[i] + dp[i], dp[i] = 2 + s[i] - s[nextVisit[i]]
        // 整合两个等式：s[i + 1] = s[i] * 2 + 2 - s[nextVisit[i]]
        // 最终的结果是所有天数之和，也就是 dp[0] + dp[1] + ... + dp[n - 2] + 1(最后一个房间只需要一次) = s[n - 1] + 1
        // 天数从 0 开始计算，只需要 s[n - 1]即可
        final long M = 1000000007;
        long[] s = new long[nextVisit.length];
        s[0] = 0;
        for (int i = 0; i < nextVisit.length - 1; i++) {
            s[i + 1] = (s[i] * 2 + 2 - s[nextVisit[i]] + M) % M;
        }
        return (int) (s[nextVisit.length - 1] % M);
    }
}

public class Main {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.firstDayBeenInAllRooms(new int[]{0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}));
    }
}
