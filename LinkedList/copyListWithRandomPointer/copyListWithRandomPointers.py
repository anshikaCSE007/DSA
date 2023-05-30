# problem statement - https://leetcode.com/problems/copy-list-with-random-pointer/description/


"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        temp = head;
        # storing head2 for newly created LL;
        head2 = None;
        temp2 = head2;

        if(not temp):
            return head;
        
        while(temp):

            if(not temp2):
                temp2 = Node(temp.val);
                head2 = temp2;
            
            else:
                newNode = Node(temp.val);
                temp2.next = newNode;
                temp2 = newNode;

            temp= temp.next;

        
        curr = head;
        temp = head2;
        
        # creating new links for having LL -  oldNode --> newNode ---> oldNode --> newNode-- ....
        while(curr):
            t = temp.next;
            temp.next = curr.next;
            curr.next = temp

            temp = t;
            curr = curr.next.next;

        # Knowing that node.random for an new node is actually nothing but adjacent node to Oldnode.random;
        curr = head;
        temp = head.next;
        while(curr):
            oldRandom = curr.random;
            if(curr.random):
                newRandom = curr.random.next;
                # print(temp.val, newRandom.val)
                temp.random = newRandom;

            curr = curr.next.next;
            if(temp.next):
                temp = temp.next.next;


        # decoupled the linked list;
        curr = head;
        head2 = curr.next;
        temp = curr.next;
        while(curr):
            curr.next = curr.next.next;
            if(temp.next):
                temp.next = temp.next.next;

            curr = curr.next;
            temp = temp.next;

        
        return head2;