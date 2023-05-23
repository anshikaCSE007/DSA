def solve(self, A):
      A = list(A);
      n = len(A);
      maxEle = max(A);
      secMax = A[0];

      for i in range(n):
          if(A[i] != maxEle and secMax < A[i]):
              secMax = A[i];
      
      return secMax%maxEle;