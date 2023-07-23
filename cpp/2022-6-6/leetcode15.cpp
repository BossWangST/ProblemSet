//
// Created by mac on 6/6/22.
//
#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

class Solution {
public:
    vector<vector<int>> threeSum(vector<int> &nums) {
        vector<vector<int>> res;
        if (nums.size() < 3)
            return res;
        /*
         * 2022-6-6 1st attempt: Is it two PTR?
         * Sort first, then L is 1!!! and R is nums.size()-1
         */
        sort(nums.begin(), nums.end());
        unordered_set<int> s;
        for (int i = 0; i < nums.size(); i++) {
            int diff = 0 - nums[i];
            if (!s.count(nums[i]))
                s.insert(nums[i]);
            else
                continue;
            //next we can use 2 ptr to find the diff
            int left = i + 1, right = nums.size() - 1;
            while (left < right) {
                int cur_sum = nums[left] + nums[right];
                if (cur_sum == diff) {
                    res.push_back(vector<int>({nums[i], nums[left], nums[right]}));
                    left++;
                    //Here we only need to update one side!
                    //But still we need to avoid repeating!
                    while (nums[left] == nums[left - 1] && left < right)
                        left++;
                } else if (cur_sum < diff) {
                    left++;
                } else {
                    right--;
                }
            }
        }
        return res;
    }
};

int main(void) {
    return 0;
}