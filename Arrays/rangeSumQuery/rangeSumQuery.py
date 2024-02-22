class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
     # @return an list of long
    def rangeSum(self, A, B):
        n = len(A);
        pf = [0]*n;
        pf[0] = A[0];
        resultantArr = [];

        for i in range(1,n):
            pf[i] = A[i] + pf[i-1];

        
        for i in range(len(B)):
            l = B[i][0];
            r = B[i][1];
            l = l-1;
            r = r-1;
            if(l==0):
                resultantArr.append(pf[r]);
            else:
                sumLR = pf[r] - pf[l-1];
                resultantArr.append(sumLR);
        
        return resultantArr;