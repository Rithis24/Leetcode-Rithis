// Last updated: 8/12/2026, 11:51:56 AM
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

        if (head == null || head.next == null || k == 0)
            return head;

        ListNode temp = head;
        int length = 1;

        while (temp.next != null) {
            temp = temp.next;
            length++;
        }

        temp.next = head;

        k = k % length;

        int stepsToNewHead = length - k;

        ListNode newTail = head;

        for (int i = 1; i < stepsToNewHead; i++) {
            newTail = newTail.next;
        }

        ListNode newHead = newTail.next;
        newTail.next = null;

        return newHead;
    }
}