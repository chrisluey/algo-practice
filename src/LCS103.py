# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def doIt(node: Optional[TreeNode], level: int) -> None:
            if node == None:
                return
            if len(result) > level:
                if level % 2 == 0:
                    result[level].append(node.val)
                else:
                    result[level].insert(0, node.val)
            else:
                result.append([node.val])
            doIt(node.left, level + 1)
            doIt(node.right, level + 1)
        doIt(root, 0)
        return result
        