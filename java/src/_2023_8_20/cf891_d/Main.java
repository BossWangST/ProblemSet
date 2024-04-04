package _2023_8_20.cf891_d;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        /*
        据说是经典套路，如果一个图的构成定义如下：
        给定 2 个数组 a 和 b
        iff a[u] - a[v] >= b[u] - b[v], there is a path from u -> v
        那么看到不等式，我们总应该先想想，要不要把不等式重新排列一下呢？
        改为 a[u] - b[u] >= a[v] - b[v] 这样子的话我们就可以构造一个新的数组 c where c[i] = a[i] - b[i]
        那么现在一条边的构成就变成了这样 如果 c[i] >= c[j] (i != j) then i -> j
        所以，每两个 c[i] 和 c[j] 都有可能形成一条边，那么如果一个节点想要连接到所有节点
        假设为节点 x，那么如果连上所有其他节点，必然是 c[x] >= c[i] for all i (i != x)
        那么排序之后最大值必然是满足要求的，找最大值的个数即可！
         */
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int[] a = new int[n];
            int[] c = new int[n];
            int m = Integer.MIN_VALUE;
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            for (int i = 0; i < n; i++) {
                int b = sc.nextInt();
                c[i] = a[i] - b;
                m = Math.max(m, c[i]);
            }
            // 导致 TLE 的经典罪魁祸首！排序！既然只要最大值，那么记住不就行了，排什么序啊
            int res = 0;
            for (int i = 0; i < n; i++) res += (c[i] == m ? 1 : 0);
            System.out.println(res);
            for (int i = 0; i < n; i++) {
                if (c[i] == m)
                    System.out.printf("%d ", i + 1);
            }
            System.out.println();
        }
    }
}
