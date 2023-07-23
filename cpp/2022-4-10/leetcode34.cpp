#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.size() == 0) return vector<int>({-1, -1});
        if (nums.size() == 1) {
            if (nums[0] == target)
                return vector<int>({0, 0});
            else
                return vector<int>({-1, -1});
        }
        int left = 0, right = nums.size() - 1;
        int mid;
        while (left < right) {
            mid = (left + right) / 2;
            if (nums[mid] < target)
                left = mid + 1;
            else {
                right = mid;
            }
        }
        int i = left + 1;
        for (; i < nums.size() && nums[left] == nums[i]; i++)
            ;
        if (nums[left] == target)
            return vector<int>({left, i - 1});
        else
            return vector<int>({-1, -1});
    }
};
int main() {
    vector<int> nums({2, 2});
    cout << (new Solution)->searchRange(nums, 1)[0] << endl;
    return 0;
}

