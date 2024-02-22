
# problem statment - https://leetcode.com/problems/spiral-matrix/description/

# better solution - easy to memorise - 
def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix);
        m = len(matrix[0]);
        res = [];
        i = 0;
        j = 0;
        
        while(n>1 and m>1):
            
            for k in range(1,m):
                res.append(matrix[i][j]);
                j+=1;
            
            for k in range(1,n):
                res.append(matrix[i][j]);
                i+=1;
                
            for k in range(1,m):
                res.append(matrix[i][j]);
                j-=1;
                
            for k in range(1,n):
                res.append(matrix[i][j]);
                i-=1;
                
                
            i+=1;
            j+=1;
            n-=2;
            m-=2;
            
        # special condition for rectangular matrix
        if(abs(n-m) >= 1):
            if(n == 1):
                for k in range(m):
                    res.append(matrix[i][j]);
                    j+=1;
                    
            elif(m == 1):
                for k in range(n):
                    res.append(matrix[i][j]);
                    i+=1;
                    
        elif(n == 1):
            res.append(matrix[i][j]);
            
            
            
        return res;
# one solutions - 
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