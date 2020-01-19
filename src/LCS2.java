/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode result = new ListNode(0);
        ListNode curr = result;
        int carry = 0;
        int val = 0;
        
        while (l1 != null || l2 != null)
        {
            if (l1 == null)
            {
                val = l2.val + carry;
                l2 = l2.next;
            }
            else if (l2 == null)
            {
                val = l1.val + carry;
                l1 = l1.next;
            }
            else
            {
                val = l1.val + l2.val + carry;
                l1 = l1.next;
                l2 = l2.next;
            }
            
            if (val > 9)
            {
                carry = 1;
                val -= 10;
            }
            else
                carry = 0;
            curr.val = val;
            if (l1 != null || l2 != null)
            {
                curr.next = new ListNode(carry);
                curr = curr.next;
            }
        }
        
        if (carry == 1)
            curr.next = new ListNode(carry);
        
        return result;
    }
}