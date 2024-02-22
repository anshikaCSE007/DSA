
# https://www.interviewbit.com/problems/pick-from-both-sides/
class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, arr, B):
        n = len(arr);
        if(B == n):
            return sum(arr);
        pf = [0]*n;
        pf[0] = arr[0];
        for i in range(1,n):
            pf[i] = pf[i-1] + arr[i]
            
        i = B-1;
        j = n;
        
        maxSumm = float("-inf");
        totalSumm = sum(arr);
        
        while(i>=-1):
            if(i<0):
                summ = pf[j-1];
            else:
                summ = pf[j-1] - pf[i];
            if((totalSumm - summ)> maxSumm):
                maxSumm = totalSumm - summ;
            i-=1;
            j-=1;
            
        return maxSumm;