# https://www.interviewbit.com/problems/multiple-left-rotations-of-the-array/


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers
    def reverseArr(self, A, st, end):
        i = st;
        j = end;
        
        while(i < j):
            temp = A[i];
            A[i] = A[j];
            A[j] = temp;
            
            i+=1;
            j-=1;
            
        
        
    def rotateArr(self, A, B):
        n = len(A);
        
        k = B%n;
        
        self.reverseArr(A, 0, n-1);
        self.reverseArr(A, 0, n-k-1);
        self.reverseArr(A, n-k, n-1);
        
        return A;
        
        
    def solve(self, A, B):
        n = len(B);
        ans = [];
        for i in range(n):
            arr = [x for x in A];
            res = self.rotateArr(arr, B[i]);
            ans.append(res);