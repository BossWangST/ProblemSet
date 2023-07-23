#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
int* getPrime(int n) {
    int* p = (int*)calloc(n + 1, sizeof(int));
    int p_num = 0;
    bool* nums = (bool*)calloc(n + 1, sizeof(bool));
    for (int i = 0; i < n + 1; i++) nums[i] = true;
    nums[0] = nums[1] = false;
    for (int i = 2; i < n + 1; i++) {
        if (nums[i]) p[p_num++] = i;
        for (int j = 0; j < p_num; j++) {
            int cur = p[j] * i;
            if (cur > n) break;
            nums[cur] = false;
        }
    }
    p[p_num] = INT_MIN;
    return p;
}
int distinctPrimeFactors(int* nums, int numsSize) {
    int prd = 1;
    for (int i = 0; i < numsSize; i++) prd = prd < nums[i] ? nums[i] : prd;
    int* p = getPrime(prd);
    int res = 0;
    int size = 0;
    int j = 0;
    while (p[j] != INT_MIN) {
        j++;
        size++;
    }
    bool* has_p = (bool*)calloc(size, sizeof(bool));
    for (int i = 0; i < numsSize; i++) {
        for (int j = 0; j < size; j++) {
            if (!has_p[j])
                if (nums[i] % p[j] == 0) {
                    has_p[j] = true;
                    res++;
                }
        }
    }
    return res;
}
int main() {
    printf("Hello world\n");
    return 0;
}

