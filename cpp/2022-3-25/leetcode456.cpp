#include <iostream>
#include <stack>
#include <vector>
using namespace std;
class Solution {
public:
    bool find132pattern(vector<int>& nums) {
        int n = nums.size();
        if (n <= 2) return false;
        int num_2 = -1000000001;
        stack<int> s;
        s.push(nums[n - 1]);
        for (int i = n - 2; i >= 0; i--) {
            if (nums[i] < num_2) return true;
            while (!s.empty() && nums[i] > s.top()) {
                num_2 = s.top();
                s.pop();
            }
            if (num_2 < nums[i]) s.push(nums[i]);
        }
        return false;
    }
};
int main() {
    vector<int> num({1, 4, 0, -1, -2, -3, -1, -2});
    cout << (new Solution)->find132pattern(num) << endl;
    return 0;
}

