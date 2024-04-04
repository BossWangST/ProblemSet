package _2023_8_17.cf892.b;

import java.util.*;

public class Main {
    static class pair {
        long a;
        long b;
        long get;

        public pair(long one, long two) {
            a = one;
            b = two;
            get = b - a;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t > 0) {
            t--;
            int n = sc.nextInt();
            long res = 0;
            long min = Integer.MAX_VALUE;
            long min2 = Integer.MAX_VALUE;
            var l = new ArrayList<pair>();
            for (int i = 0; i < n; i++) {
                var cur = new ArrayList<Integer>();
                int len = sc.nextInt();
                for (int j = 0; j < len; j++) cur.add(sc.nextInt());
                Collections.sort(cur);
                l.add(new pair(cur.get(0), cur.get(1)));
                res += cur.get(1);
                min = Math.min(min, cur.get(0));
                min2 = Math.min(min2, cur.get(1));
            }
            // l.sort(Comparator.comparingLong(i -> i.b));
            // 找到最小的 第二小数！ -> 收益最低
            // 注意到，如果要移走数列的一个数，必然是移走最小的，那么暴露出来的就是第二小的数
            // 为了最大化收益，肯定第二小的数最小的一个来存放其他移动进来的数字
            // 最终形成的结果就是 拥有最小的第二小数的数组贡献最小数，其余数组贡献第二小数！
            // 计算起来就是 res = sum(第二小数) + 最小数 - 最小的第二小数
            res += min - min2;
            System.out.println(res);
        }
    }
}


