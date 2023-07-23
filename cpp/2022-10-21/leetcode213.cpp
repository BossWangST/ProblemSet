//
// Created by bossw on 2022/10/21.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int rob_not_circle(vector<int> &nums) {
        int rob1, rob2;
        rob1 = rob2 = 0;
        for (int i = 0; i < nums.size(); i++) {
            int newRob = max(rob1 + nums[i], rob2);
            rob1 = rob2;
            rob2 = newRob;
        }
        return rob2;
    }

    int rob(vector<int> &nums) {
        vector<int> no_head = nums;
        no_head.erase(no_head.begin());
        vector<int> no_tail = nums;
        no_tail.erase(no_tail.begin() + no_tail.size() - 1);
        return max(nums[0], max(rob_not_circle(no_head), rob_not_circle(no_tail)));
    }
};

int main(void) {
    vector<int> nums{1, 1, 3, 6, 7, 10, 7, 1, 8, 5, 9, 1, 4, 4, 3};
    cout << (new Solution)->rob(nums) << endl;
    return 0;
}