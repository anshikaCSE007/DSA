problem - stat


class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse = True);

        ans = 0;

        for i in range(len(A)):
            ans += A[i]*(i+1);

        return ans;