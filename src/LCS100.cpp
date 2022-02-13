/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        vector<TreeNode*> pqueue;
        vector<TreeNode*> qqueue;
        pqueue.push_back(p);
        qqueue.push_back(q);
        while (!pqueue.empty() && !qqueue.empty()) {
            if ((!pqueue.empty()) != (!qqueue.empty())) {
                return false;
            }
            TreeNode* pcurr = pqueue.back();
            TreeNode* qcurr = qqueue.back();
            if ((!pcurr == NULL) != (!qcurr == NULL)) {
                return false;
            }
            if (pcurr == NULL && qcurr == NULL) {
                pqueue.pop_back();
                qqueue.pop_back();
                continue;
            }
            if (pcurr->val != qcurr->val) {
                return false;
            }
            pqueue.pop_back();
            qqueue.pop_back();
            pqueue.push_back(pcurr->left);
            pqueue.push_back(pcurr->right);
            qqueue.push_back(qcurr->left);
            qqueue.push_back(qcurr->right);
        }
        return true;
    }
};