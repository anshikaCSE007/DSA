
class Solution:
    def maxLen(self, n, arr):
        #Code here
        hm = { arr[0]: 0 };
        ans = 0;
        if(arr[0] == 0):
            ans = 1;
        
            
        for i in range(1,n):
            # if(arr[i] == 0):
            #   ans =
            arr[i] += arr[i-1];
            if(arr[i] == 0):
                ans = i+1;
            if(arr[i] in hm):
                ans = max(ans, i-hm[arr[i]]);
            else:
                hm[arr[i]] = i;
            
        return ans;
