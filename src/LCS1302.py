# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        lvl, result, stack = 1, 0, []
        stack.append((root, 1))
        while len(stack) > 0:
            curr = stack.pop()
            if curr[0] == None:
                continue
            if curr[1] == lvl:
                result += curr[0].val
            elif curr[1] > lvl:
                result = curr[0].val
                lvl = curr[1]
            stack.append((curr[0].left, curr[1] + 1))
            stack.append((curr[0].right, curr[1] + 1))
        return result