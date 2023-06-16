

# problem statment - https://practice.geeksforgeeks.org/problems/nearly-sorted-1587115620/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


import heapq;
class Solution:
    
    #Function to return the sorted array.
    def nearlySorted(self,a,n,k):
        
        # code here
        res = [];
        temp = [a[i] for i in range(k+1)];
        heapq.heapify(temp);
        
        for i in range(k+1, n):
            minEle = heapq.heappushpop(temp, a[i]);
            res.append(minEle);
            
        
        while(len(temp)):
            res.append(heapq.heappop(temp));
            
            
        return res;
            
            
            