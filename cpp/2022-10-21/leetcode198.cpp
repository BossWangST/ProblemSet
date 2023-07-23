//
// Created by bossw on 2022/10/21.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int rob(vector<int> &nums) {
        vector<int> table(nums.size() + 1, 0);
        table[0] = 0;
        table[1] = nums[0];
        int max_rob = max(table[0], table[1]);
        if (nums.size() == 1)
            return table[nums.size()];
        for (int i = 2; i < table.size(); i++) {
            int cur_max = -1;
            for (int j = 0; j < i - 1; j++) {
                cur_max = max(cur_max, table[j]);
            }
            table[i] += cur_max + nums[i - 1];
            max_rob = max(max_rob, table[i]);
        }
        return max_rob;
    }
};

int main(void) {
    vector<int> nums{2, 1, 1, 2};
    cout << (new Solution)->rob(nums) << endl;
    return 0;
}