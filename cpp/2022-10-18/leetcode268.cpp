//
// Created by bossw on 2022/10/18.
//
#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

class Solution {
public:
    int missingNumber(vector<int> &nums) {
        int n = nums.size();
        vector<bool> bucket(n + 1, false);
        for (int i = 0; i < n; i++) {
            bucket[nums[i]] = true;
        }
        for (int i = 0; i < n + 1; i++) {
            if (!bucket[i])
                return i;
        }
        return -1;
    }
};

int main() {
    vector<int> nums{3, 0, 1};
    cout << (new Solution)->missingNumber(nums) << endl;
    return 0;
}