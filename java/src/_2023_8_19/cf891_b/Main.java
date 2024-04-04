package _2023_8_19.cf891_b;

import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t-- > 0) {
            String s = "";
            s = sc.next();
            int l = s.length();
            char[] chr = s.toCharArray();
            int[] nums = new int[l];
            for (int i = 0; i < l; i++) nums[i] = chr[i] - '0';
            int zero = 0;
            for (int i = l - 1; i > 0; i--) {
                boolean in = false;
                while (i > 0 && nums[i] >= 5) {
                    if (!in) in = true;
                    zero = i;
                    i--;
                    nums[i]++;
                }
                if (in) i++;
            }
            if (nums[0] >= 5) {
                System.out.println("1" + "0".repeat(l));
            }
            else if (zero == 0) System.out.println(s);
            else {
                for (int i = 0; i < zero; i++)
                    System.out.printf("%d", nums[i]);
                System.out.println("0".repeat(l - zero));
            }
        }
    }
}
