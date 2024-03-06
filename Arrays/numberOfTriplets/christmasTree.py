


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        n = len(A);
        ans = float("inf");
        for i in range(n):
            
            l = float("inf");
            for j in range(i-1, -1, -1):
                if(A[j] < A[i]):
                    l = min(l, B[j]);

            
            r = float("inf");
            for j in range(i+1, n):
                if(A[j] > A[i]):
                    r = min(r, B[j]);


            if(l != float("inf") and r != float("inf")):
                ans = min(ans, (l+r+B[i]));

        
        if(ans != float("inf")):
            return ans;

        return -1;