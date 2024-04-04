package _2023_8_18.cf893_b;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n, m, d;
            n = sc.nextInt();
            m = sc.nextInt();
            d = sc.nextInt();
            // int[] shop = new int[m];
            ArrayList<Integer> shop = new ArrayList<>();
            shop.add(1 - d); // 把头当作 1 - d，这样就是必然在 1 处要吃糖了
            for (int i = 0; i < m; i++) shop.add(sc.nextInt());
            // 吃不吃糖，不需要一个个考虑，因为吃糖必然是一个等差数列，比如 d = 2 的时候，假设在 i 处吃了一颗，那么 i + d 要吃，i + 2 * d 也要吃
            // 所以，吃糖的总数就是，既然开头就要吃一个，我们就把开头也当作一个 shop 来统一
            // 那么在路上吃糖（不在 shop 吃）的总数就是 res = (S.i - S.(i - 1) - 1) // d 即每 2 个 shop 之间（不算自己）到底吃了多少糖
            // 比如 d = 2，1 和 4 有 shop 那么 1 2 3 4，1 和 4 之间的距离是 3，此时必然吃了 1 颗
            // 如果 d = 2，1 和 3 有 shop 那么 1 2 3，1 和 3 之间的距离为 2，虽然此时走了 2 步应该吃，但是和 3 号所在地的 shop 重合了
            // 所以要在距离上 -1 来避免这个问题
            shop.add(n + 1); // 看走到终点的时候还要不要吃
            int res = m; // init
            /*
            如何判断去除一个 shop 后的 res？很简单，就是减去有他在时的计算，再加上没他时的计算
            如果去除第 i 个 shop
            new_res = res - (S.i - S.(i - 1) - 1) // d - (S.(i + 1) - S.i - 1) // d + (S.(i + 1) - S.(i - 1) - 1) // d
            我们要 new_res 越小越好！
             */
            int sub = Integer.MIN_VALUE; // 减的越多越好！
            ArrayList<Integer> sub_shop = new ArrayList<>();
            for (int i = 1; i < m + 1; i++) {
                int front = shop.get(i) - shop.get(i - 1) - 1;
                int back = shop.get(i + 1) - shop.get(i) - 1;
                int mid = shop.get(i + 1) - shop.get(i - 1) - 1;
                res += front / d;
                int cur = front / d + back / d - mid / d;
                if (cur > sub) {
                    sub = cur;
                    sub_shop.clear();
                }
                if (cur == sub) {
                    sub_shop.add(i);
                }
            }
            res += (shop.get(m + 1) - shop.get(m) - 1) / d; // 处理尾巴，看走到最后要不要吃
            res = res - sub - 1;
            System.out.println(res + " " + sub_shop.size());
        }
    }
}
