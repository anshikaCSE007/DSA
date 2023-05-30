

# problem statement - https://leetcode.com/problems/merge-two-sorted-lists/description/

def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      h1 = list1;
      h2 = list2;

      if((not list1 and not list2) or (not list2)):
          return list1;

      if(not list1):
          return list2;

      if(list1.val <= list2.val):
          h3 = list1;
          h1 = h1.next;

      else:
          h3 = list2;
          h2 = h2.next;

      last = h3;
      while(h1 and h2):


          if(h1.val <= h2.val):
              last.next = h1;
              h1 = h1.next;
              last = last.next;
          
          else:
              last.next = h2;
              h2 = h2.next;
              last = last.next;

      
      if(h1):
          last.next = h1;
      
      else:
          last.next = h2;

      return h3;