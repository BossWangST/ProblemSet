//
// Created by mac on 6/1/22.
//
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    vector<int> productExceptSelf(vector<int> &nums) {
        vector<int> output(nums.size());
        output[0] = 1;
        // 2 passes. First to get the original suffix
        int cur_prdt = 1;//current_product
        for (int i = 0; i < nums.size() - 1; i++) {
            cur_prdt *= nums[i];
            output[i + 1] = cur_prdt;
        }
        cur_prdt = 1;
        //Second pass to get the original suffix
        for (int i = nums.size() - 1; i > 0; i--) {
            cur_prdt *= nums[i];
            output[i - 1] *= cur_prdt;
        }
        return output;
    }
    /*
     * 2022-6-1:1st attempt:
     * after seeing the video for some part, we know that we can make 2 arrays
     * one is prefix, one is suffix to save the product from left to right & right to left
     * then if we want to calculate res[i], we can simply calculate prefix[i-1] times suffix[i+1]
     * 2nd attempt:
     * No need for prefix and suffix. Also be cautious that O(2*n) is still O(n)
     */
};

int main(void) {

}