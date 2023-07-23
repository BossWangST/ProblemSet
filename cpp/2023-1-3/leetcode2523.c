#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* getPrime(int n) {
    int* p = (int*)calloc(n + 1, sizeof(int));
    bool* num = (bool*)calloc(n + 1, sizeof(bool));
    int p_num = 0;
    for (int i = 0; i < n + 1; i++) num[i] = true;
    num[0] = num[1] = false;
    int cur;
    for (int i = 2; i < n + 1; i++) {
        if (num[i]) p[p_num++] = i;
        for (int j = 0; j < p_num; j++) {
            cur = p[j] * i;
            if (cur > n) break;
            num[cur] = false;
        }
    }
    p[p_num] = INT_MIN;
    return p;
}
int* closestPrimes(int left, int right, int* returnSize) {
    int* p = getPrime(right);
    int j = 0;
    int size = 0;
    while (p[j] != INT_MIN) {
        size++;
        j++;
    }
    int* res = (int*)calloc(2, sizeof(int));
    int diff = INT_MAX;
    for (int i = 0; i < size - 1; i++) {
        if (p[i] < left) continue;
        if (p[i + 1] - p[i] < diff) {
            res[0] = p[i];
            res[1] = p[i + 1];
            diff = p[i + 1] - p[i];
        }
    }
    if (diff == INT_MAX) res[0] = res[1] = -1;

    *returnSize = 2;
    return res;
}
int main() {
    printf("Hello world\n");
    return 0;
}

