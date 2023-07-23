//
// Created by mac on 6/12/22.
//
#include<iostream>
#include<vector>

using namespace std;


class Solution {
public:
    int getSum(int a, int b) {
        int res = a ^ b;
        int carry = a & b;
        int temp;
        while (carry != 0) {
            carry = (unsigned int) carry << 1;
            temp = res;
            res ^= carry;
            carry &= temp;
        }
        return res;
    }
};

int main(void) {
    cout << (new Solution)->getSum(-1, 1) << endl;
    return 0;
}
