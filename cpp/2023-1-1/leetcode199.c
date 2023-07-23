#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode* left;
    struct TreeNode* right;
};

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
typedef struct {
    struct TreeNode** arr;
    int head, tail;
    int size, capacity;
} Queue;
Queue* createQ(int capacity) {
    Queue* new = (Queue*)malloc(sizeof(Queue));
    new->head = new->size = 0;
    new->tail =
        capacity - 1;  // HERE IS THE KEY: This makes pushQ functions correctly:
                       // when 1st element enters, then (tail+1)%capacity -> 0
    new->capacity = capacity;
    new->arr = (struct TreeNode**)calloc(capacity, sizeof(struct TreeNode*));
    return new;
}

bool isQEmpty(Queue* q) { return q->size == 0; }

bool isQFull(Queue* q) { return q->size == q->capacity; }

bool pushQ(Queue* q, struct TreeNode* val) {
    if (isQFull(q)) return false;
    q->tail = (q->tail + 1) % q->capacity;
    q->arr[q->tail] = val;
    q->size++;
    return true;
}

struct TreeNode* popQ(Queue* q) {
    if (isQEmpty(q)) return NULL;
    struct TreeNode* res = q->arr[q->head];
    q->head = (q->head + 1) % q->capacity;
    q->size--;
    return res;
}

int* rightSideView(struct TreeNode* root, int* returnSize) {
    int* res = (int*)calloc(100, sizeof(int));
    int p = 0;
    int cur_level = 1;  // root
    int new_level = 0;
    Queue* q = createQ(100);
    pushQ(q, root);
    while (!isQEmpty(q)) {
        struct TreeNode* cur = popQ(q);
        cur_level--;
        if (cur->left != NULL) {
            pushQ(q, cur->left);
            new_level++;
        }
        if (cur->right != NULL) {
            pushQ(q, cur->right);
            new_level++;
        }
        if (cur_level == 0) {
            res[p++] = cur->val;
            cur_level = new_level;
            new_level = 0;
        }
    }
    *returnSize = p;
    return res;
}
int main() {
    Queue* q = createQ(100);
    struct TreeNode* root = (struct TreeNode*)malloc(sizeof(struct TreeNode));
    root->val = 100;
    root->left = root->right = NULL;
    pushQ(q, root);
    struct TreeNode* cur = popQ(q);
    printf("%d\n", cur->val);
    return 0;
}
