

class Solution:
    # @param A : list of list of integers
    # @param B : list of list of integers
    # @return a list of list of integers
    def solve(self, A, B):
        n = len(A);
        m = len(A[0]);
        matrix = []

        for i in range(n):
            matrix.append([])
            for j in range(m):
                matrix[i].append(0);

        
        for i in range(n):
            for j in range(m):
                matrix[i][j] = A[i][j] - B[i][j];
        
        return matrix;