
# youtube link - https://www.youtube.com/watch?v=nP_ns3uSh80
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 0 1 2 3 4 5 6 7 8 9 10 11
        # 2 2 1 1 3 1 3 3 3 3 4 3

        c = 1;
        ele = nums[0];


        for i in range(1, len(nums)):
            if(nums[i] == ele):
                c +=1;
            
            else:
                c-=1;

            if(c == 0):
                c = 1;
                ele = nums[i];

        return ele;



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0;
        n = len(nums);
        
        for i in range(n):
            if(cnt == 0):
                ele = nums[i];
                cnt+=1;
                
                
            elif(nums[i] == ele):
                cnt+=1;
                
            else:
                cnt-=1;
                
                
        
        c = 0;
        for i in range(n):
            if(ele == nums[i]):
                c+=1;
                
        if(c >= n//2):
            return ele;
        
        return -1;