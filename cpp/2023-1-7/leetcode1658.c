#include <limits.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MIN(a, b) ((a) < (b) ? (a) : (b))

int minOperations(int* nums, int numsSize, int x) {
    int sum = 0;
    for (int i = 0; i < numsSize; i++) sum += nums[i];
    if (sum < x) return -1;
    int left, right, l_sum, r_sum;
    left = -1;  // no left sum
    right = 0;  // whole array become right sum
    l_sum = 0;
    r_sum = sum;
    int res = INT_MAX;
    // KEY: left++ -> sum +
    // right++ -> sum -
    for (; left < numsSize; left++) {
        if (left >= 0) l_sum += nums[left];
        while (l_sum + r_sum > x && right < numsSize)
            r_sum -= nums[right++];  // if l_sum + r_sum > x -> sum needs - ->
                                     // right++
        if (l_sum + r_sum == x) res = MIN(res, left + 1 + numsSize - right);
    }
    return res == INT_MAX ? -1 : res;
}
int main() {
    int nums[] = {1, 1, 4, 2, 3};
    printf("%d\n", minOperations(nums, 5, 5));
    return 0;
}

