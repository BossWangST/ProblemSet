//
// Created by bossw on 2022/10/23.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    bool canJump(vector<int> &nums) {
        int target = nums.size() - 1;
        int i = target - 1;
        while (target > 0 && i >= 0) {
            if (i >= 0 && nums[i] >= (target - i)) {
                target = i;
                i = target - 1;
            } else
                i--;
        }
        if (target <= 0)
            return true;
        else
            return false;
    }
};

int main(void) {
    vector<int> nums{2, 0, 0};
    cout << (new Solution)->canJump(nums) << endl;
    return 0;
}