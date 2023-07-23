//
// Created by bossw on 2022/10/19.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int coinChange(vector<int> &coins, int amount) {
        vector<long long> table(amount + 1, 1 << 30);
        table[0] = 0;
        for (long long i = 0; i < amount + 1; i++) {
            for (long long j = 0; j < coins.size(); j++) {
                if (i + coins[j] < amount + 1) {
                    if (table[i + coins[j]] > table[i] + 1) {
                        table[i + coins[j]] = table[i] + 1;
                    }
                }
            }
        }
        if (table[amount] == (1 << 30))
            return -1;
        else
            return table[amount];
    }
};

int main(void) {
    vector<int> coins{1, 2, 5};
    cout << (new Solution)->coinChange(coins, 11) << endl;
    return 0;
}