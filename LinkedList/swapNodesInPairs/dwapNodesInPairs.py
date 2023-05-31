# problem statement - https://leetcode.com/problems/swap-nodes-in-pairs/description/

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(not head):
            return head;
        temp = head;
        newHead = head.next;

        if(not head.next):
            return head;

        prev = None;
        while(temp):
            t = temp;
            nextT = temp.next;
            if(nextT):
                t.next = t.next.next;
                nextT.next = t;

            if(prev and nextT):
                prev.next = nextT;
            prev = temp;
            temp = temp.next;


        return newHead;