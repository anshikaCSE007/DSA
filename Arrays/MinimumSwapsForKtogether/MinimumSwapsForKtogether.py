

class Solution:
        
    def minSwap (self,A, n, B) : 
        #Complete the function
        size = 0;
        n = len(A);
        for i in range(n):
            if(A[i] <= B):
                size+=1;


        swaps = 0;

        for i in range(size):
            if(A[i] > B):
                swaps+=1;

        minSwaps = swaps;
        # print(minSwaps)

        i = 1;
        j = size;

        while(i <= n-size and j < n):
            if(A[i-1] > B):
                swaps-=1;

            if(A[j] > B):
                swaps+=1;

            minSwaps = min(minSwaps, swaps);

            i+=1;
            j+=1;

        return minSwaps;