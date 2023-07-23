//
// Created by mac on 1/7/23.
//


#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<string.h>

int xorBeauty(int *nums, int numsSize) {
    int res = nums[0];
    for (int i = 1; i < numsSize; i++)
        res ^= nums[i];
    return res;
}

int main(void) {
    printf("Hello World\n");
    return 0;
}
