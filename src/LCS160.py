# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pointerA, pointerB = headA, headB
        while pointerA != pointerB:
            if pointerA == None:
                pointerA = headB
            else:
                pointerA = pointerA.next
            if pointerB == None:
                pointerB = headA
            else:
                pointerB = pointerB.next
        return pointerA