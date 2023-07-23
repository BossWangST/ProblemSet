#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int bi_search(vector<int>& nums, int left, int right, int target) {
        int mid;
        while (left < right) {
            mid = (left + right) / 2;
            if (nums[mid] < nums[right]) {  // right part is in order
                int disorder = bi_search(nums, left, mid - 1, target);
                if (-1 == disorder) {
                    if (nums[mid] < target)  // target is in the ordered part
                        left = mid + 1;
                    else if (nums[mid] == target)
                        return mid;
                    else
                        // target is in the disordered part
                        return bi_search(nums, left, mid - 1, target);
                } else
                    return disorder;
            } else {  // left part is in order
                int disorder = bi_search(nums, mid + 1, right, target);
                if (-1 == disorder) {
                    if (nums[mid] > target)  // target is in the ordered part
                        right = mid - 1;
                    else if (nums[mid] == target)
                        return mid;
                    else
                        // target is in the disordered part
                        return bi_search(nums, mid + 1, right, target);
                } else
                    return disorder;
            }
        }
        if (nums[left] == target)
            return left;
        else
            return -1;
    }
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        return bi_search(nums, left, right, target);
    }
};
int main() {
    vector<int> nums({3, 1});
    cout << (new Solution)->search(nums, 3) << endl;
    return 0;
}

