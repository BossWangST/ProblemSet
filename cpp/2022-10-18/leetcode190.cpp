//
// Created by bossw on 2022/10/18.
//

#include<iostream>
#include<vector>

using namespace std;

class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t res = 0;
        uint32_t cutter = 1;
        for (int i = 0; i < 31; i++) { // !! Here is 31 not 32, a bit left shift 31 times, it'll come to head!
            if ((cutter & n) != 0) {
                res |= 1;
                res <<= 1;
            } else
                res <<= 1;
            cutter <<= 1;
        }
        // !! So here, DO NOT FORGET LAST BIT!
        if ((cutter & n) != 0) {
            res |= 1;
        }
        return res;
    }
};

int main(void) {
    cout << (new Solution)->reverseBits(43261596) << endl;
    return 0;
}