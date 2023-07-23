#include <iostream>
#include <set>
#include <vector>
using namespace std;
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.size() <= 2) return nums.size();
        vector<int>::iterator itor = nums.begin();
        while (itor != nums.end()) {
            if (*itor == *(itor + 1) && *(itor + 1) == *(itor + 2)) {
                itor += 2;
                if (itor == nums.end()) break;
                while (itor != nums.end() && *itor == *(itor - 1))
                    itor = nums.erase(itor);
            } else
                itor++;
        }
        return nums.size();
    }
};
int main() {
    vector<int> nums({1, 1, 2, 2});
    cout << (new Solution)->removeDuplicates(nums) << endl;
    return 0;
}

