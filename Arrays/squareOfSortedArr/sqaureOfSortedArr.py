

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums);
        
        for i in range(n):
            nums[i] = nums[i]*nums[i];
            
        
        head = 0;
        tail = n-1;
        
        res = [0]*n;
        
        j = n-1;
        
        while(head <= tail):
            if(nums[head] > nums[tail]):
                res[j] = nums[head];
                head+=1;
                
            elif(nums[head] <= nums[tail]):
                res[j] = nums[tail];
                tail-=1;
                
            j-=1;
            
        return res;
        