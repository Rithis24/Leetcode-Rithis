// Last updated: 8/12/2026, 11:50:10 AM
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
    public ListNode reverseList(ListNode head) {
            ListNode c=head;
            ListNode p=null;
            while(c!=null){
                ListNode next=c.next;
                c.next=p;
                p=c;
                c=next;
            }
            return p;
    }
}