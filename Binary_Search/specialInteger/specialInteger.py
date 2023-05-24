

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def maxSubArraySum(self, A, k, B):
        n =len(A);
        summ = 0;
        maxSum = 0;
        if k == n:
            return sum(A)
        for i in range(k):
            summ+=A[i];

        i=1;
        j=k;

        while(i<=n-1 and j<=n-1):
            summ = summ-A[i-1]+A[j];
            maxSum = max(maxSum, summ);
            if(maxSum > B):
                return maxSum;
            i+=1;
            j+=1;

        return maxSum;

    def solve(self, A, B):
        ans = 0;
        l=1;
        h=len(A);

        while(l<=h):
            mid = (l+h)//2;
            maxSum = self.maxSubArraySum(A,mid,B);
            if(maxSum <= B):
                ans = mid;
                l = mid+1;
            
            else:
                h = mid-1;

        
        return ans;