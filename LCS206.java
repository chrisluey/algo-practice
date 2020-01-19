/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */

import java.util.*;

class Solution {
    public ListNode reverseList(ListNode head) {
        
        if (head == null)
        {
            return head;
        }
        Stack<Integer> stack = new Stack();
        ListNode curr = head;
        
        while (curr != null)
        {
            stack.push(curr.val);
            curr = curr.next;
        }
        
        curr = head;
        while(!stack.empty())
        {
            curr.val = stack.pop();
            curr = curr.next;
        }
        return head;
    }
}