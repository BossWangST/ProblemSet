package _2023_8_20.cf891_c;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int l = n * (n - 1) / 2;
            int[] b = new int[l];
            for (int i = 0; i < l; i++) b[i] = sc.nextInt();
            int [] a = new int[n];
            Arrays.sort(b);
            int cur_min = Integer.MAX_VALUE;
            Arrays.fill(a, Integer.MAX_VALUE);
            int p = 0; // track array b
            for (int i = 0; i < n; i++) {
                for (int j = i + 1; j < n; j++) {
                    // for each pair <i, j>, assign smaller one to a[i]
                    a[i] = Math.min(a[i], b[p++]);
                }
            }
            a[n - 1] = a[n - 2];
            for (int v : a) System.out.printf("%d ", v);
            System.out.println();
        }
    }
}
