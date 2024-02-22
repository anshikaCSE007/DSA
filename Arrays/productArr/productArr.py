class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums);
        pfp = [1]*n;
        sfp = [1]*n;
        pfp[0] = nums[0];
        sfp[n-1] = nums[n-1]
        for i in range(1,n):
            pfp[i] = pfp[i-1]*nums[i];
        
        for i in range(n-2, -1, -1):
            sfp[i] = sfp[i+1]*nums[i];
            
        
        productArr = [1]*n;
        
        for i in range(n):
            
            if(i == 0):
                prod = sfp[i+1];
                
            elif(i == n-1):
                prod = pfp[i-1];
                
            else:
                prod = pfp[i-1]*sfp[i+1];
            
            
            productArr[i] = prod;
            
        
        return productArr;
                
        