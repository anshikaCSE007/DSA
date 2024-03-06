class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix);
        
        for j in range(n):
            for i in range(n//2):
                temp = matrix[i][j];
                matrix[i][j] = matrix[n-i-1][j]
                matrix[n-i-1][j] = temp;
        print(matrix)
        i = 0;

        for i in range(n):
            for k in range(i+1, n):
                temp = matrix[i][k];
                matrix[i][k] = matrix[k][i]
                matrix[k][i] = temp;
                
        return matrix;