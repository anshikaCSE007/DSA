

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        res = [];
        r = len(A);
        c = len(A[0]);

        for i in range(r):
            res.append([]);
            for j in range(c):
                res[i].append(A[i][j] + B[i][j]);


        return res;