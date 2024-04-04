#include<iostream>
using namespace std;

class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        if (nums.size() == 0) return vector<string>();
        int start = nums[0];
        vector<string> res;
        if (nums.size() == 1) {res.push_back(to_string(nums[0])); return res;}
        for (int i = 1; i < nums.size(); i++) {
            if ((long long)nums[i] - nums[i - 1] == 1) continue;
            if (nums[i - 1] == start) res.push_back(to_string(nums[i - 1]));
            else res.push_back(to_string(start) + "->" + to_string(nums[i - 1]));
            start = nums[i];
        }
        if (nums[nums.size() - 1] == start) res.push_back(to_string(nums[nums.size() - 1]));
        else res.push_back(to_string(start) + "->" + to_string(nums[nums.size() - 1]));
        return res;
    }
};

int main(void) {
    vector<int> nums{0,2,3,4,6,8,9};
    auto res = (new Solution)->summaryRanges(nums);
    return 0;
}