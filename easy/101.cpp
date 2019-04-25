bool fun(TreeNode *p, TreeNode *q) {
    if(p == NULL && q == NULL) return true;
    if((p == NULL && q != NULL) || (p != NULL && q == NULL)) return false;
    if(p->val != q->val) return false;
    else {
        if(!fun(p->left, q->right)) return false;
        if(!fun(p->right, q->left)) return false;
        else return true;
    }

}

class Solution {
public:
    bool isSymmetric(TreeNode *root) {
        if(root == NULL) return true;
        return fun(root->left, root->right);
    }
};