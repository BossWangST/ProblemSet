#include <iostream>
#include <set>
#include <vector>
using namespace std;
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int one = 0, two = 0;
        for (int i = 0; i < nums.size(); i++) {
            one = one ^ nums[i] & (~two);
            // two = (nums[i] == 0) ? two : (one == 1) ? two : ~two;
            two = two ^ nums[i] & (~one);
        }
        return one;
        /* set<int> one, two; */
        /* for (int i = 0; i < nums.size(); i++) { */
        /*     if (one.find(nums[i]) == one.end()) { */
        /*         if (two.find(nums[i]) == two.end()) one.insert(nums[i]); */
        /*     } else { */
        /*         one.erase(nums[i]); */
        /*         two.insert(nums[i]); */
        /*     } */
        /* } */
        /* return *one.begin(); */
    }
};
int main() { return 0; }

