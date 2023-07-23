//
// Created by bossw on 2022/10/19.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int lengthOfLIS(vector<int> &nums) {
        vector<int> table(nums.size(), 1);
        int max_num = 1;
        for (int i = 0; i < nums.size(); i++) {
            int local_max = 1;
            bool flag = false; // True <> find someone smaller than nums[i] behind i
            for (int j = i - 1; j >= 0; j--) {
                // * search table behind 'i', find the LIS, then add
                if (nums[j] < nums[i]) {
                    local_max = max(local_max, table[j]);
                    flag = true;
                }
            }
            if (flag) {
                table[i] += local_max;
                max_num = max(max_num, table[i]);
            }
        }
        return max_num;
    }
};

int main(void) {
    vector<int> nums{0, 1, 0, 3, 2, 3};
    cout << (new Solution)->lengthOfLIS(nums) << endl;
    return 0;
}