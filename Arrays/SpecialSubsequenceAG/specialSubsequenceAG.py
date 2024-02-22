

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A);
        c = 0;
        ans = 0;
        for i in range(n-1, -1, -1):
            if(A[i] == 'G'):
                c+=1;
            elif(A[i] == 'A'):
                ans+=c;
        return ans%(10**9 + 7);