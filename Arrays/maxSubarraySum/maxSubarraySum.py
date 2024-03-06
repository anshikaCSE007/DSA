

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums);
        maxSumm = max(max(nums), sum(nums));
        summ = 0;
        for i in range(n):
            summ += nums[i];
            
            if(summ > 0):
                maxSumm = max(maxSumm, summ)
                
            else:
                summ = 0;
        
        return maxSumm;
                