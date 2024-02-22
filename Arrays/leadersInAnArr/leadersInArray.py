

class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, n):
        #Code here
        idxs = set([n-1]);
        res = [];
        
        maxRight = A[n-1];
        
        for i in range(n-2, -1, -1):
            if(A[i] >= maxRight):
                maxRight = A[i];
                idxs.add(i);
        
        for i in range(n):
            if(i in idxs):
                res.append(A[i]);
                
                
        return res;