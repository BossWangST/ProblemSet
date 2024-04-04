package _2023_9_27.leetcode1333;

import java.util.*;

class Solution {
    public List<Integer> filterRestaurants(int[][] restaurants, int veganFriendly, int maxPrice, int maxDistance) {
        HashMap<Integer, int[]> d = new HashMap<>();
        int cnt = 0;
        for (int i = 0; i < restaurants.length; i++) {
            if (restaurants[i][2] < veganFriendly || restaurants[i][3] > maxPrice || restaurants[i][4] > maxDistance)
                continue;
            d.put(restaurants[i][0], restaurants[i]); // <id, restaurant>
            cnt++;
        }
        var res = new int[cnt][5]; // id starts from 1
        int k = 0;
        for (int key : d.keySet())
            res[k++] = d.get(key);
        Arrays.sort(res, (o1, o2) -> {
            if (o1[1] > o2[1])
                return -1;
            else if (o1[1] < o2[1])
                return 1;
            else {
                if (o1[0] < o2[0])
                    return 0;
                else
                    return -1;
            }
        });
        var l_res = new ArrayList<Integer>();
        for (int i = 0; i < res.length; i++) {
            l_res.add(res[i][0]);
        }
        /*
        var real_res = new ArrayList<Integer>();
        for (int i = 0; i < cnt; i++)
            real_res.add(l_res.get(restaurants.length - i - 1));

         */
        return l_res;
    }
}

public class Main {
    public static void main(String[] args) {
        var s = new Solution();
        int[][] restaurants = new int[][]{{1, 4, 1, 40, 10}, {2, 8, 0, 50, 5}, {3, 8, 1, 30, 4}, {4, 10, 0, 10, 3}, {5, 1, 1, 15, 1}};
        System.out.println(s.filterRestaurants(restaurants, 0, 50, 10));
    }
}
