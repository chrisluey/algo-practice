# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = None
        curr = head
        prev = None
        while curr != None:
            if prev == None:
                prev = curr
            elif prev.val == curr.val:
                while curr != None and prev.val == curr.val:
                    curr = curr.next
                if slow == None:
                    head = curr
                else:
                    slow.next = curr
                prev = curr
                if curr == None:
                    break
            else:
                if slow == None:
                    head = prev
                slow = prev
                prev = curr
            curr = curr.next
        return head