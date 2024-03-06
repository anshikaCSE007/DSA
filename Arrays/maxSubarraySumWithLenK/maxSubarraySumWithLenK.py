

class Solution:
    def maximumSumSubarray (self,k,Arr,N):
        # code here 
        n = len(Arr);
        
        pf = [0]*n;
        pf[0] = Arr[0];
        
        for i in range(1,n):
            pf[i] = pf[i-1] + Arr[i];
            
            
        i = 0;
        j = k-1
        summ  = 0;
        while(i<=j and i<n and j<n):
            if(i==0):
                tempSum = pf[j];
                
            else:
                tempSum = pf[j] - pf[i-1];
                
                
            
            summ = max(summ, tempSum);
            
            i+=1;j+=1;
            
        return summ;