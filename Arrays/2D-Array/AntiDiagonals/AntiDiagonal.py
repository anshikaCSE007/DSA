


class Solution:
    # @param A : list of list of integers
    # @return a list of list of integers
    def diagonal(self, A):
        n = len(A);

        res = [];
        n = len(A);
        d = 2*n-1;
        
        for i in range(d):
            res.append([]);
            for j in range(n):
                res[i].append(0);

        i = 0;
        j = 0;
        for k in range(n):
            c = k;
            r = 0;
            j = 0;
            while(c>=0 and r<n):
                res[i][j] = A[r][c];
                r+=1;
                c-=1;
                j+=1;

            i+=1;

        for k in range(1, n):
            c = n-1;
            r = k;
            j = 0;
            while(c>=0 and r<n):
                res[i][j] = A[r][c];
                r+=1;
                c-=1;
                j+=1;

            i+=1;

        return res;