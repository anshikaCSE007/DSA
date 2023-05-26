
# problem statement - https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        hm = { arr[0]: 1 };
        ans = 0;
        if(arr[0] == 0):
            return True;
        
            
        for i in range(1,n):
            if(arr[i] == 0):
                return 1;
            arr[i] += arr[i-1];
            if(arr[i] in hm or arr[i] == 0):
                return True;
            
            hm[arr[i]] = 1;
            
        
        return False;