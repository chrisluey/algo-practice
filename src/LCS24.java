/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        if (head == null || head.next == null) {
            return head;
        }
        ListNode temp = head.next;
        head.next = temp.next;
        temp.next = head;
        ListNode temp2 = head.next;
        if (temp2 == null || temp2.next == null) {
            return temp;
        }
        ListNode temp3 = temp2.next;
        while (temp2.next != null) {
            temp2.next = temp3.next;
            
            temp3.next = temp2;
            head.next = temp3;
            head = temp2;
            if (temp2.next == null) {
                break;
            }
            
            temp2 = temp2.next;
            if (temp2.next == null) {
                break;
            }
            temp3 = temp2.next;
            
        }
        return temp;
        
    }
}