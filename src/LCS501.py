# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        this_dict = {}
        queue = []
        queue.append(root)
        while len(queue) > 0:
            curr = queue.pop(0)
            if curr == None:
                continue
            if this_dict.get(curr.val) == None:
                this_dict[curr.val] = 1
            else:
                this_dict[curr.val] += 1
            queue.append(curr.left)
            queue.append(curr.right)
        max_value = 0
        for key, value in this_dict.items():
            if value >= max_value:
                max_value = value
        result = []
        for key, value in this_dict.items():
            if value == max_value:
                result.append(key)
        return result
        