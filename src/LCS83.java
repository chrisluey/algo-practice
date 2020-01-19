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
    public ListNode deleteDuplicates(ListNode head) {
        HashSet<Integer> set = new HashSet();
        ListNode curr = head;
        if (curr == null)
        {
            return curr;
        }
        set.add(curr.val);
        curr = curr.next;
        while (curr != null)
        {
           if (set.contains(curr.val))
           {
               ListNode next = curr.next;
               curr.next = next.next;
           }
            curr = curr.next;
        }
        return head;
    }
}