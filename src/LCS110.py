# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, node: TreeNode, height: int) -> int:
        if node == None:
            return height
        left = self.helper(node.left, height + 1)
        right = self.helper(node.right, height + 1)
        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right)
        
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, 0) != -1
    
    
        