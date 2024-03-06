

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = [];
        
        
        n = len(matrix);
        m = len(matrix[0]);
        
        for j in range(m):
            ele = [];
            for i in range(n):
                ele.append(matrix[i][j]);
                
            res.append(ele);
            
            
        return res;


# without extra space only works for nxn matrix.

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix);
        i = 0;

        for i in range(n):
            for j in range(i+1, n):
                temp = matrix[i][j];
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp;

        return matrix;
