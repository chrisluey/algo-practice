# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        result = root
        if p == root or q == root:
            return result
        while True:
            if p.val > result.val and q.val > result.val:
                result = result.right
            elif p.val < result.val and q.val < result.val:
                result = result.left
            else:
                break
        return result