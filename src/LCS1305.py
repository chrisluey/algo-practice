# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def getInts(this_node: TreeNode, this_list: List[int]) -> None:
            if this_node == None:
                return
            getInts(this_node.left, this_list)
            this_list.append(this_node.val)
            getInts(this_node.right, this_list)
        list1 = []
        list2 = []
        getInts(root1, list1)
        getInts(root2, list2)
        result = []
        i,j = 0,0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        while i < len(list1):
            result.append(list1[i])
            i += 1
        while j < len(list2):
            result.append(list2[j])
            j += 1
        return result
        
       