class Solution {
public:
    bool isSameTree(TreeNode *p, TreeNode *q) {
        if(p == NULL && q == NULL) return true;
        if((p == NULL && q != NULL) || (p != NULL && q == NULL)) return false;
        if(p->val == q->val) {
            // 左子树不是相同的树
            if(!isSameTree(p->left, q->left)) return false;
            // 右子树不是相同的树
            if(!isSameTree(p->right, q->right)) return false;
            else return true;
        } else {
            return false;
        }

    }
};