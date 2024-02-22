class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A);
        maxN = max(A);
        minN = min(A);
        ans = n;
        maxi = -1;
        mini = -1;
        if(maxN == minN):
            return 1;
        for i in range(n-1, -1, -1):
            if(A[i] == maxN):
                maxi = i;

            elif(A[i] == minN):
                mini = i;

            if(maxi != -1 and mini != -1):
                l = abs(maxi - mini) + 1;

                ans = min(ans, l);

        return ans;