

class Solution:

	def maxIndexDiff(self,A,n):
		#code here
		n = len(A);
        temp = [];

        for i in range(n):
            temp.append([A[i], i]);

        temp.sort();

        rightMaxIdx = 0;
        maxDiff = float("-inf");

        for k in range(n-1, -1, -1):
            i = temp[k][1];
            j = rightMaxIdx;

            if(j >= i):
                maxDiff = max(maxDiff, (j-i));

            if(rightMaxIdx < temp[k][1]):
                rightMaxIdx = temp[k][1];


        return maxDiff;