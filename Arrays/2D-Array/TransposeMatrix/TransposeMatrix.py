

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