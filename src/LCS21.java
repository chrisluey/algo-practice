/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode result = new ListNode();
        if (l1 != null && l2!= null) {
            if (l1.val <= l2.val) {
                result.val = l1.val;
                l1 = l1.next;
            } else {
                result.val = l2.val;
                l2 = l2.next;
            }
        } else if (l1 != null) {
            result.val = l1.val;
            l1 = l1.next;
        } else if (l2 != null) {
            result.val = l2.val;
            l2 = l2.next;
        }else {
            result = null;
            return result;
        }
        ListNode curr = result;
        while (l1 != null || l2 != null) {
            if (l1 == null) {
                curr.next = new ListNode(l2.val);
                curr = curr.next;
                l2 = l2.next;
            } else if (l2 == null) {
                curr.next = new ListNode(l1.val);
                curr = curr.next; 
                l1 = l1.next;
            } else if (l1.val <= l2.val) {
                curr.next = new ListNode(l1.val);
                curr = curr.next;
                l1 = l1.next;
            } else {
                curr.next = new ListNode(l2.val);
                curr = curr.next;
                l2 = l2.next;
            }
        }
        return result;
    }
}