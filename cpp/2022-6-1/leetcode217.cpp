//
// Created by mac on 6/1/22.
//
#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int> &nums) {
        unordered_set<int> s;
        bool dup = false;
        for (int i = 0; i < nums.size(); i++) {
            if (s.count(nums[i]))
                dup = true;
            s.insert(nums[i]);
        }
        return dup;
    }
    /*
     * 2022-6-1:1st attempt:Hash Set is ok.
     */
};

int main(void) {
    return 0;
}