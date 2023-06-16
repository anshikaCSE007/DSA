
# problem statment - https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix);
        col = len(matrix[0]);

        startRow = 0;
        startCol = 0;
        rowEnd = rows-1
        colEnd = col-1;
        res = [];

        while( rowEnd >= 0 and startRow <= rowEnd and colEnd >=0 and  startCol <= colEnd):
            i = startRow;
            j = startCol;

            while(startCol <= j<= colEnd and startRow<=i<=rowEnd):
                res.append(matrix[i][j]);
                j+=1;

            j = j-1;
            i = i+1;
            while(startCol <= j<= colEnd and startRow<=i<=rowEnd):
                res.append(matrix[i][j]);
                i+=1;

            j = j-1;
            i = i-1;
            while(startCol <= j <= colEnd and startRow<i<=rowEnd):
                res.append(matrix[i][j]);
                j-=1;

            j = j+1;
            i = i-1;
            while(startCol <= j < colEnd and startRow < i < rowEnd):
                res.append(matrix[i][j]);
                i-=1;


                    
            j
            startRow +=1;
            startCol +=1;
            rowEnd-=1;
            colEnd-=1;

        
        return res;