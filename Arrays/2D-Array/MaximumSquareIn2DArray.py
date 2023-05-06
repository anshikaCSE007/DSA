
# problem statement - https://www.interviewbit.com/problems/maximum-sum-square-submatrix/
# Approach - 1 
# Brute Force - O(n^4);

def solve(self, A, B):
        row = len(A);
        col = len(A[0]);
        maxSum = float('-inf');
        
        for i in range(row):
            for j in range(col):
                
                # i---> i+B;
                # j---> j+B;
                summ = 0;
                if(i+B <= row and j+B <= col):
                    for k in range(i, i+B):
                        for l in range(j, j+B):
                            summ += A[k][l];
                            
                    maxSum = max(maxSum, summ)
        
        return maxSum;




# Approach - 2
# Prefix Sum - contstruct - O(n*m);
# find each summ - O(n*m);



def solve(self, A, B):

        n = len(A);
        m = len(A[0]);
        maxSum = float('-inf');

        pfMat = [[0]*m for i in range(n)];

        for i in range(n):
            for j in range(m):
                pfMat[i][j] += A[i][j];

                if(i > 0):
                    pfMat[i][j] += pfMat[i-1][j];

                if(j > 0):
                    pfMat[i][j] += pfMat[i][j-1];

                if(i>0 and j>0):
                    pfMat[i][j] -= pfMat[i-1][j-1];

        for i in range(n):
            for j in range(m):
                sx = i;
                ex = i+B-1;
                sy = j;
                ey = j+B-1;

                if(ey < m and ex < n):
                    summ = pfMat[ex][ey];
                    if(sy > 0):
                        summ -= pfMat[ex][sy-1];
                    if(sx > 0):
                        summ -= pfMat[sx-1][ey];
                    if(sx > 0 and sy>0):
                        summ += pfMat[sx-1][sy-1];
                    maxSum = max(maxSum, summ);
        
        return maxSum;