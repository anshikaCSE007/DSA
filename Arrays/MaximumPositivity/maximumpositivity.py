


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        n = len(A);

        l = 0;
        ans = 0;
        st = -1;
        end = -1;
        maxSt = 0;
        minSt = 0;

        for i in range(n):
            if(A[i] > 0):
                l+=1;

                if(st == -1):
                    st = i;

                end = i;

                if(l > ans):
                    minSt = st;
                    maxSt = end;

                ans = max(ans, l);

            else:
                st = -1;
                end = -1;
                l = 0;


        return A[minSt:maxSt+1];