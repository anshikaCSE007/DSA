# problem statement - https://practice.geeksforgeeks.org/problems/maximum-sum-rectangle2948/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article



class Solution:
    def rowWiseKedan(self, mat):
        summ = 0;
        maxSum = float('-inf');
        startIdx = -1;
        endIdx  = -1;

        for i in range(len(mat)):
            summ += mat[i];
            if(startIdx < 0):
                startIdx = i;
            if(maxSum < summ):
                maxSum = summ;
            if(summ < 0):
                summ = 0;
                startIdx = -1;
            endIdx = i;
            
        return maxSum, startIdx, endIdx;
    def maximumSumRectangle(self,R,C,A):
        #code here
        n = len(A);
        m = len(A[0]);
        maxSum  = float('-inf');
        left = 0;
        right  = 0;
        maxLeft = 0;
        maxRight = 0;
        maxUp = 0;
        maxDown = 0;

        for i in range(m):
            temp = [0]*n;
            for j in range(i, m):
                
                for k in range(n):
                    temp[k] += A[k][j];
                summ, upIdx, downIdx = self.rowWiseKedan(temp)
                if(maxSum < summ):
                    maxSum = max(maxSum, summ);
                    maxLeft = i;
                    maxRight = j;
                    maxUp = upIdx;
                    maxDown = downIdx;
        print(maxLeft, maxUp, maxRight, maxDown)
        return maxSum;