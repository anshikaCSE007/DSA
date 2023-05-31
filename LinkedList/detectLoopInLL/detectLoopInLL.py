
# using hashSet: 

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def solve(self, head):
        setA = set();
        temp = head;
        prev = None;
        while(temp):
            if(temp in setA):
                prev.next = None;
                temp = None;
            else:
                setA.add(temp);
                prev = temp;
                temp = temp.next;

        return head;


# using slow and fast pointer
