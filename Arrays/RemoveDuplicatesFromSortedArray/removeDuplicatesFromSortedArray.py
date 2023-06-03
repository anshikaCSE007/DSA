
# problem statement - https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      n = len(nums);
      num = nums[0];
      

      i = 0;

      # 0   1   2   3   4   5
      # 1   1   e   2   2   3
      #             i       j
      #         c = 1;
      #         c = 2
      
      while(i < n):
          j = i+1;
          c = 1;
          while(i<j and j<n):

              # nums[i] and nums[j] equal;
              if(nums[i] == nums[j]):
                  c+=1;
                  if(c > 2):
                      nums[j] = 'e';
                  j+=1;
              
              elif(nums[i] != nums[j]):
                  i = j;

          if(j==n):
              break;

      i = 0;
      j = 1;

      while(i<n and j<n):

          if(nums[i] == 'e' and nums[j] == 'e'):
              j+=1;
          
          elif(nums[i] == 'e' and nums[j] != 'e'):
              print(i)
              temp = nums[j];
              nums[i] = temp;
              nums[j] = 'e';
              print(nums)
              i+=1;
              j+=1;
          
          else:
              i+=1;
              j+=1;


      k = 0;

      while(k<n):
          if(nums[k] == 'e'):
              break;
          k+=1;



          


      print(nums)

      return k;