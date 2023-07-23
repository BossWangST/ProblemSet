//
// Created by mac on 6/1/22.
//
#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution {
public:
    int maxProfit(vector<int> &prices) {
        /*2022-6-1:1st attempt
         * Key: Buy low, Sell high.
         * So since we need to check a RANGE in which we want to maximum the profit,
         * we can use the technic TWO PTR, where Left is buy and Right is sell.
        */
        if (prices.size() == 1)
            return 0;
        int left = 0, right = 1;
        int cur_max = 0;//2nd attempt: init cur_max to 0 is better!
        while (right < prices.size()) {
            if (prices[right] < prices[left]) {
                // sell price < buy price
                left = right;
                right++;
            } else {
                cur_max = (prices[right] - prices[left]) > cur_max ? (prices[right] - prices[left]) : cur_max;
                right++;
            }
        }
        return cur_max;
    }
};

int main(void) {
    vector<int> prices({7, 1, 5, 3, 6, 4});
    cout << (new Solution)->maxProfit(prices) << endl;
    return 0;
}