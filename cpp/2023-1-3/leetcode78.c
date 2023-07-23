#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *returnColumnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume
 * caller calls free().
 */
bool* visited;
int** res;
int size;
void dfs(int cur_size, int* returnSize, int* nums, int** returnColumnSizes) {
    if (cur_size == size) {
        int num = 0;
        for (int i = 0; i < size; i++)
            if (visited[i]) num++;
        if (num == 0) {
            res[*returnSize] = NULL;
            (*returnColumnSizes)[*returnSize] = num;
            (*returnSize)++;
            return;
        }
        res[*returnSize] = (int*)calloc(num, sizeof(int));
        int j = 0;
        for (int i = 0; i < size; i++)
            if (visited[i]) res[*returnSize][j++] = nums[i];
        (*returnColumnSizes)[*returnSize] = num;
        (*returnSize)++;
        return;
    }
    visited[cur_size] = false;
    dfs(cur_size + 1, returnSize, nums, returnColumnSizes);
    visited[cur_size] = true;
    dfs(cur_size + 1, returnSize, nums, returnColumnSizes);
}
int** subsets(int* nums, int numsSize, int* returnSize,
              int** returnColumnSizes) {
    res = (int**)calloc(1 << numsSize, sizeof(int*));
    visited = (bool*)calloc(numsSize, sizeof(bool));
    size = numsSize;
    *returnSize = 0;
    // returnColumnSizes = (int**)malloc(sizeof(int**));
    (*returnColumnSizes) = (int*)calloc(1 << numsSize, sizeof(int));
    dfs(0, returnSize, nums, returnColumnSizes);
    return res;
}
int main() {
    int nums[] = {1, 2, 3};
    int returnSize;
    int** returnColumnSizes = (int**)malloc(sizeof(int*));
    int** res = subsets(nums, 3, &returnSize, returnColumnSizes);
    for (int i = 0; i < returnSize; i++) {
        for (int j = 0; j < (*returnColumnSizes)[i]; j++)
            printf("%d\t", res[i][j]);
        printf("\n");
    }
    return 0;
}

