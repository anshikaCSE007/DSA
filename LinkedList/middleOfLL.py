
# problem statement - https://leetcode.com/problems/middle-of-the-linked-list/description/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head;
        fast = head;

        while(fast and fast.next):
            slow = slow.next;
            fast = fast.next.next;

        return slow