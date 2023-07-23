//
// Created by bossw on 2022/10/19.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        vector<int> table(n + 1, 0);
        table[1] = 1;
        if (n == 1)
            return 1;
        table[2] = 2;
        for (int i = 3; i < n + 1; i++) {
            table[i] = table[i - 2] + table[i - 1];
        }
        return table[n];
    }
};

int main(void) {
    cout << (new Solution)->climbStairs(3) << endl;
    return 0;
}