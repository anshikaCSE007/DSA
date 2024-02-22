

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        m = len(A);
        n = len(A[0]);
        p = len(B[0]);
        matrix = [];

        for i in range(m):
            matrix.append([]);
            for j in range(p):
                matrix[i].append(0);
            
        for i in range(m):
            for j in range(p):
                for k in range(n):
                     matrix[i][j] += A[i][k] * B[k][j]
        
        return matrix;