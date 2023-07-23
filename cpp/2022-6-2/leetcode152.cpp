//
// Created by mac on 6/2/22.
//
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int maxProduct(vector<int> &nums) {
        /*
         * 2022-6-2:1st attempt:
         * Same idea with Max_subarray_sum
         * drop product that is negative.
         * No! if there are 2 negatives, then the product will be positive!
         *
         * 2nd attempt:
         * Dynamic Programming
         * we need to keep track of 2 dp table: max_prdt & min_prdt
         * Why? Since there are negatives in the array, we can use the min times negative ones to get a
         * greater product.
         *
         * 3rd attempt:
         * Do we actually need two arrays? Not at all!
         * We just need two int cur_max & cur_min.
         */
        int cur_max, cur_min;
        cur_max = cur_min = 1;
        int res = -1000001;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) {
                cur_max = cur_min = 1;
                res = max(0, res);
                continue;
            }
            int mul_max = nums[i] * cur_max;
            int mul_min = nums[i] * cur_min;
            cur_max = max(nums[i], max(mul_max, mul_min));
            cur_min = min(nums[i], min(mul_max, mul_min));
            res = max(res, cur_max);
        }
        return res;
    }
};

int main(void) {
    vector<int> nums({1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4});
    cout << (new Solution)->maxProduct(nums) << endl;
    return 0;
}