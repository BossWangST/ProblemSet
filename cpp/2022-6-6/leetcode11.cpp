//
// Created by mac on 6/6/22.
//
#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    int maxArea(vector<int> &height) {
        /*
         * 2022-6-6 1st attempt: 2 ptr
         */
        int left = 0, right = height.size() - 1;
        int cur_max = 0;
        int cur_area = (right - left) * min(height[left], height[right]);
        while (left < right) {
            cur_max = max(cur_max, cur_area);
            int l_step = (right - left - 1) * min(height[left + 1], height[right]);
            int r_step = (right - 1 - left) * min(height[left], height[right - 1]);
            //Here is the key:since we have max the width, then we need to max the height as high as possible!
            //So the small one should be stepped over while the taller one is still.
            if (height[left] < height[right]) {
                cur_area = l_step;
                left++;
            } else {
                cur_area = r_step;
                right--;
            }
        }
        return cur_max;
    }
};

int main(void) {
    vector<int> height({1, 3, 2, 5, 25, 24, 5});
    cout << (new Solution)->maxArea(height) << endl;
    return 0;
}