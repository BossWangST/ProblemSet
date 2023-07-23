#include <limits.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/**
 * Definition for a binary tree node.
 */
struct TreeNode {
    int val;
    struct TreeNode *left;
    struct TreeNode *right;
};

int res;
void dfs(struct TreeNode *node, int cur_max) {
    if (node == NULL) return;
    if (node->val >= cur_max) res++;
    cur_max = cur_max > node->val ? cur_max : node->val;
    dfs(node->left, cur_max);
    dfs(node->right, cur_max);
    return;
}
int goodNodes(struct TreeNode *root) {
    res = 0;
    dfs(root, INT_MIN);
    return res;
}
int main() { return 0; }

