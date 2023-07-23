//
// Created by bossw on 2023/6/9.
//

#include <stdio.h>

int findTargetSumWays(int *nums, int numsSize, int target) {
    int s = 0;
    int end = (1 << numsSize) - 1;
    int res = 0;
    int cur, k, i;
    while (s <= end) {
        cur = 0;
        k = (1 << (numsSize - 1));
        for (i = 0; i < numsSize; i++) {
            if ((k & s) > 0)
                cur -= nums[i];
            else
                cur += nums[i];
            k >>= 1;
        }
        if (cur == target)
            res++;
        s++;
    }
    return res;

}

int main(void) {
    int nums[] = {1, 1, 1, 1, 1};
    printf("%d\n", findTargetSumWays(nums, 5, 3));
    return 0;
}