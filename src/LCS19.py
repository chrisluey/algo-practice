# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def listSize(node: ListNode) -> int:
            result = 1
            while (node.next != None):
                node = node.next
                result += 1
            return result
        
        skips = listSize(head) - n
        i = 1
        curr = head
        while i < skips:
            curr = curr.next
            i += 1
        if skips == 0:
            if head.next != None:
                head = head.next
            else:
                head = None
        elif curr.next != None:
            temp = curr.next
            curr.next = temp.next
            del temp
        else:
            del curr
        return head
            