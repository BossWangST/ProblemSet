//
// Created by mac on 6/5/22.
//
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int findMin(vector<int> &nums) {
        /*
         * 2022-6-5 1st attempt: binary search
         * every binary search, we'll get 2 subarray, and
         * one must be in order!
         * Also, the left ordered part is always bigger than the right part!
         */
        int left, mid, right;
        left = 0, right = nums.size() - 1;
        int min_num = 5001;
        while (left <= right) {
            mid = (left + right) / 2;
            if (nums[mid] > nums[right]) {
                //nums[mid] is in the left ordered part, then the min one must be in the right somewhere
                left = mid + 1;
            } else {
                //nums[mid] is in the right ordered part, which is what we want.
                right = mid - 1;
                min_num = min(nums[mid], min_num);
            }
        }
        return min_num;
    }
};

int main(void) {
    vector<int> nums({11,13,15,17});
    cout << (new Solution)->findMin(nums) << endl;
    return 0;
}