package _2023_8_19.cf893_c;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            // 既然要 gcd 的种类多，那么每一个数字来，都让他成为 gcd 即可（if possible）
            ArrayList<Integer> res = new ArrayList<>();
            boolean[] vis = new boolean[n];
            for (int i = 1; i <= n; i++) {
                if (vis[i - 1]) continue;
                res.add(i);
                int cur = 2 * res.get(res.size() - 1);
                while (cur <= n) {
                    // 每个数字怎么成为 gcd？找其最小的倍数！
                    res.add(cur);
                    vis[cur - 1] = true;
                    cur *= 2;
                }
                vis[i - 1] = true;
            }
            for (int val : res) System.out.printf("%d ", val);
            System.out.println();
        }
    }
}
