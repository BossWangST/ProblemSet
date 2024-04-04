package _2023_8_19.cf893_a;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            int n = sc.nextInt();
            int x = 0; // # of odd
            int y = 0; // # of even
            for (int i = 0; i < n; i++) {
                if ((sc.nextInt() & 1) == 1) x++;
                else y++;
            }
            if ((x & 1) == 1) System.out.println("NO");
            else System.out.println("YES");
        }
    }
}
