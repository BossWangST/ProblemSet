#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct Trie {
    struct Trie** tab;
    int cnt;
} Trie;
Trie* createTrie(int size) {
    Trie* new = (Trie*)malloc(sizeof(Trie));
    new->tab = (Trie**)calloc(size, sizeof(Trie*));
    for (int i = 0; i < size; i++) new->tab[i] = NULL;
    new->cnt = 0;
    return new;
}
void insertTrie(Trie* root, int num) {
    int and_cnt = 14;
    int cur;
    for (int i = 0; i < 15; i++, and_cnt--) {
        cur = (num >> and_cnt) & 1;
        if (root->tab[cur] == NULL) root->tab[cur] = createTrie(2);
        root = root->tab[cur];
        root->cnt++;
    }
}
int checkTrie(Trie* root, int cur, int limit) {
    /*
     * when limit's current bit is 0: XOR->0->continue; XOR->1->OVER
     * when limit's current bit is 1: XOR->0->SUCCESS; XOR->1->continue
     */
    int and_cnt = 14;
    int res = 0;
    int limit_bit;
    int cur_bit;
    for (int i = 0; i < 15; i++, and_cnt--) {
        cur_bit = (cur >> and_cnt) & 1;
        limit_bit = (limit >> and_cnt) & 1;
        // printf("%d\t|0|1|<->%d\t%d\t", i, root->tab[0] == NULL ? 0 : 1,
        //        root->tab[1] == NULL ? 0 : 1);
        // printf("%d\t%d\tcnt=%d\n", cur_bit, limit_bit, root->cnt);
        if (limit_bit == 0) {
            // XOR->0->continue
            // 0 0 or 1 1
            if (root->tab[cur_bit] != NULL)
                root = root->tab[cur_bit];
            else
                return res;
        } else {
            // XOR->0->SUCCESS
            // 0 0 or 1 1
            if (root->tab[cur_bit] != NULL) res += root->tab[cur_bit]->cnt;
            // XOR->1->continue
            // 1 0 or 0 1
            if (root->tab[cur_bit ^ 1] == NULL) return res;
            root = root->tab[cur_bit ^ 1];
        }
    }
    // equal
    res += root->cnt;
    return res;
}
int func(int* nums, int numsSize, int limit) {
    Trie* root = createTrie(2);
    int res = 0;
    for (int i = 1; i < numsSize; i++) {
        insertTrie(root, nums[i - 1]);
        res += checkTrie(root, nums[i], limit);
        printf("%d\n", res);
        // printf("----------------------------------------------------\n");
    }
    return res;
}
int countPairs(int* nums, int numsSize, int low, int high) {
    return func(nums, numsSize, high) - func(nums, numsSize, low - 1);
}
int main() {
    int nums[] = {1, 2, 4, 7};
    printf("%d\n", countPairs(nums, 4, 2, 6));
    return 0;
}

