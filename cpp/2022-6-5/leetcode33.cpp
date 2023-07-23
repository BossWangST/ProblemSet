//
// Created by mac on 6/5/22.
//
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int search(vector<int> &nums, int target) {
        /*
         * 2022-6-5 1st attempt:Seems to be the same trick as find min_num in rotated array
         *
         * after some wrong answer.
         * Key tips: 1. do not forget nums[mid]==target
         * 2. target should either be in [left,mid] or [mid,right] 闭区间!
         * 3. when using lower_bound, using vector.begin()+left/mid/right to decide the range!
         */
        int left, mid, right;
        left = 0, right = nums.size() - 1;
        while (left <= right) {
            mid = (left + right) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] > nums[right]) {
                //nums[mid] is in the left ordered part.
                if (nums[left] <= target && target <= nums[mid]) {
                    //the target is just in the ordered [left,mid]
                    vector<int>::iterator low = lower_bound(nums.begin() + left, nums.begin() + mid, target);
                    if (*low == target)
                        return low - nums.begin();
                }
                left = mid + 1;
            } else {
                //nums[mid] is in the right ordered part.
                if (nums[mid] <= target && target <= nums[right]) {
                    //the target is just in the ordered [mid,right]
                    vector<int>::iterator low = lower_bound(nums.begin() + mid, nums.begin() + right, target);
                    if (*low == target)
                        return low - nums.begin();
                }
                right = mid - 1;
            }
        }
        return -1;
    }
};

int main(void) {
    vector<int> nums({3,5,1});
    cout << (new Solution)->search(nums, 3) << endl;
    return 0;
}