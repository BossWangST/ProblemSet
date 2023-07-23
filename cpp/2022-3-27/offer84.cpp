#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        // vector<bool> buck(21, false);
        // vector<int> uni_nums;
        // int n = nums.size();
        // for (int i = 0; i < n; i++) {
        //     if (buck[nums[i]] == false) {
        //         buck[nums[i]] = true;
        //         uni_nums.push_back(nums[i]);
        //     }
        // }
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        int n = nums.size();
        do {
            vector<int> current;
            for (int i = 0; i < n; i++) current.push_back(nums[i]);
            res.push_back(current);
        } while (next_permutation(nums.begin(), nums.end()));
        return res;
    }
};
int main() {
    std::cout << "Hello world" << std::endl;
    return 0;
}

