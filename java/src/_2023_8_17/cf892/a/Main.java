package _2023_8_17.cf892.a;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t > 0) {
            t--;
            int n = sc.nextInt();
            int[] a = new int[n];
            for (int i = 0; i < n; i++) a[i] = sc.nextInt();
            Arrays.sort(a);
            int p = n - 1;
            ArrayList<Integer> b, c;
            b = new ArrayList<>();
            c = new ArrayList<>();
            while (p > 0) if (a[p] == a[p - 1]) {
                p--;
                c.add(a[p]);
            } else break;
            c.add(a[p--]);
            if (p == -1) {
                System.out.println(-1);
                continue;
            }
            while (p >= 0)
                b.add(a[p--]);
            System.out.println(b.size() + " " + c.size());
            for (Integer integer : b) System.out.printf("%d ", integer);
            System.out.println();
            for (Integer integer : c) System.out.printf("%d ", integer);
            System.out.println();
        }
    }
}
