//
// Created by mac on 6/1/22.
//
#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    int maxSubArray(vector<int> &nums) {
        int cur_sum = 0;
        /*
         * 2022-6-2:1st attempt:after watching the video, we know that
         * the KEY is to drop any negative prefix in the subarray
         */
        int cur_max = -1000000001;
        for (int i = 0; i < nums.size(); i++) {
            if (cur_sum < 0)
                cur_sum = 0;//drop negative prefix
            cur_sum += nums[i];
            //cout << cur_sum << endl;
            cur_max = cur_sum > cur_max ? cur_sum : cur_max;
        }
        return cur_max;
    }
};

int main(void) {
    vector<int> nums({-2, 1, -3, 4, -1, 2, 1, -5, 4});
    cout << (new Solution)->maxSubArray(nums) << endl;
    return 0;
}