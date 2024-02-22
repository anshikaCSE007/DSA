class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums);
        pfe = [0]*n;
        pfo = [0]*n;
        
        pfe[0] = nums[0];
        
        for i in range(1, n):
            if(i%2 == 0):
                pfe[i] = pfe[i-1] + nums[i];
                pfo[i] = pfo[i-1];
                
            else:
                pfe[i] = pfe[i-1];
                pfo[i] = pfo[i-1] + nums[i];
                
        count = 0;
        for i in range(n):
            se = pfo[n-1] - pfo[i];
            so = pfe[n-1] - pfe[i];
            
            if(i != 0):
                se = se + pfe[i-1];
                so = so + pfo[i-1];
                
                
            if(se == so):
                count+=1;
                
        return count;
            