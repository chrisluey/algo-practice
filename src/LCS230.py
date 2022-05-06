# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nums = []
        def checkNode(node: TreeNode, nums: List[int]):
            if node == None:
                return
            checkNode(node.left, nums) 
            nums.append(node.val)
            checkNode(node.right, nums)
        checkNode(root, nums)
        return nums[k-1]