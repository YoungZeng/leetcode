class Solution {
public:
    int maxDepth(TreeNode *root) {
        if(root == NULL) return 0;
        int depthL = maxDepth(root->left);
        int depthR = maxDepth(root->right);
        return 1 + (depthL > depthR ? depthL : depthR);
    }
};
