

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        temp = head;
        B = left;
        C = right;
        # head1 = A;
        k = B;
        c = 1;
        head2 = None;
        head1 = head;
        while(temp and c <=C):
            if(c == B-1):
                head1 = temp;
                temp = temp.next;
                c+=1;
            elif(c == B):
                h1 = temp;
                h3 = temp;
                while(h1 and c<=C):
                    t = h1;
                    h1 = h1.next;
                    t.next = head2;
                    head2 = t;
                    c+=1;
            else:
                temp = temp.next;
                c+=1;

        head1.next = head2;
        h3.next = h1;

        if(B == 1):
            return head2;
        
        return head;