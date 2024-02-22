class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A);
        m = len(A[0]);
        res = [];
        for j in range(m):
            summ = 0;
            for i in range(n):
                summ+=A[i][j];

            res.append(summ);

        return res;