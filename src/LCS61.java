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
    public ListNode rotateRight(ListNode head, int k) {
        if (k == 0 || head == null || head.next == null) {
            return head;
        }
        Deque<ListNode> deque = new LinkedList<>();
        ListNode curr = head;
        deque.push(curr);
        while (curr.next != null) {
            deque.push(curr.next);
            curr = curr.next;
        }
        if (k > deque.size()) {
            k = k % deque.size();
        }
        curr = deque.pop();
        while (k > 0) {
            ListNode prev = deque.peek();            
            curr.next = head;
            prev.next = null;
            head = curr;
            curr = deque.pop();
            deque.addLast(head);
            k -= 1;
        }
        return head;
    }
}