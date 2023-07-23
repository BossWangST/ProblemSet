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

bool dfs(struct TreeNode* left, struct TreeNode* right) {
    if (left != NULL && right != NULL) {
        if (left->val == right->val)
            return dfs(left->left, right->right) &&
                   dfs(left->right, right->left);
    } else if (left == NULL && right == NULL)
        return true;
    return false;
}
bool isSymmetric(struct TreeNode* root) {
    if (root == NULL) return false;
    return dfs(root->left, root->right);
}
int main() {
    printf("Hello world\n");
    return 0;
}

