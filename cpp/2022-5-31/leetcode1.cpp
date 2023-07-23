#include <iostream>
#include <vector>
#include<unordered_map>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> m;//value:index
        int i = 0;
        for (; i < nums.size(); i++) {
            if (m.count(target - nums[i])) {
                if (m[target - nums[i]] == i)
                    continue;
                return vector<int>({i, m[target - nums[i]]});
            }
            m[nums[i]] = i;
        }
        if (m.count(target - nums[i])) {
            return vector<int>({i, m[target - nums[i]]});
        }
        return vector<int>({-1, -1});
    }
    /* 2022-5-31: 1st attempt
     * Double pointer. One from left to right, one from right to left.
     * So sort first.
     * Sadly :( NO!
     * So 2nd attempt:
     * HashMap value -> index , why?
     * because for every num in nums, we ONLY want to know if (target-num) exist in nums,
     * and what it's index.
     * KEY TIP: We should firstly check if the HashMap has (target-num), then add the
     * value:index to the HashMap!
     * This is because if you add first, then two same num will be re-added to the map,
     * which will cause trouble. E.g. {3, 3}, target=6.
    */
};

int main() {
    vector<int> nums({3, 2, 4});
    vector<int> res = (new Solution)->twoSum(nums, 6);
    cout << res[0] << " " << res[1] << endl;
    return 0;
}
