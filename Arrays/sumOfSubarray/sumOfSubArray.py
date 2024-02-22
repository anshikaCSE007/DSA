# https://www.geeksforgeeks.org/problems/sum-of-subarrays2229/1


class Solution:
    def subarraySum(self, a, n):
        # code here 
        summ = 0;
        for i in range(n):
            contri = a[i]*(i+1)*(n-i);
            summ += contri
            
        return summ