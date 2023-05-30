
# problem statement - https://leetcode.com/problems/reverse-linked-list/description/

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head2 = None;
        temp = head;

        while(temp):
            t = temp;
            temp = temp.next;
            t.next = head2;
            head2 = t;
        
        return head2;