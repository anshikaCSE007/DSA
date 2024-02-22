class Solution:
    # @param A : list of integers
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        l = len(A)
        pf = [0]*l;
        res = [];
        pf[0] = 0;
        for i in range(1, l):
            if(A[i-1] <= A[i]):
                pf[i] =  0;
            else:
                pf[i] =  1
            
            pf[i] += pf[i-1] 

        for j in range(len(B)):
            left = B[j][0];
            right = B[j][1];
            factor = pf[right] - pf[left];
            if(factor == 0):
                res.append(1);
            else:
                res.append(0);

        return res  