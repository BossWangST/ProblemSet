package _2024_3_14.leetcode299;

import java.util.*;

class Solution {
    public String getHint(String secret, String guess) {
        var d = new HashMap<Character, Integer>();
        for (char c : secret.toCharArray()) {
            d.put(c, d.getOrDefault(c, 0) + 1);
        }
        int bull = 0, cow = 0, n = secret.length();
        for (int i = 0; i < n; i++) {
            char sc = secret.charAt(i); // secret char
            char gc = guess.charAt(i); // guess char
            if (sc == gc) {
                d.put(sc, d.get(sc) - 1);
                bull++;
            }
        }
        for (int i = 0; i < n; i++) {
            char sc = secret.charAt(i); // secret char
            char gc = guess.charAt(i); // guess char
            if (sc != gc) {
                if (d.getOrDefault(gc, 0) > 0) {
                    d.put(gc, d.get(gc) - 1);
                    cow++;
                }
            }
        }
        return bull + "A" + cow + "B";
    }
}

public class Main {
    public static void main(String[] args) {
        var s = new Solution();
        System.out.println(s.getHint("1122", "1222"));
    }
}
