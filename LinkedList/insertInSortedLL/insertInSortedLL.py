# problem statement - https://practice.geeksforgeeks.org/problems/insert-in-a-sorted-list/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

class Solution:
    def sortedInsert(self, head1,key):
        # code here
        # return head of edited linked list
        ele = key;
        temp = head1
        t = Node(key)
        if(not head1):
            return t;
        if(head1 and ele <= head1.data):
            t.next = temp;
            head1 = t;
            return head1;
            
        while(temp and temp.next):
            if(temp.data < ele and temp.next.data >= ele):
                t.next = temp.next;
                temp.next = t;
                return head1;
            
            temp = temp.next;
                
        
        temp.next = t;
        
        return head1;