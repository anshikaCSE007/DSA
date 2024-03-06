

class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A);
        total1s = 0;

        for i in range(n):
            if(A[i] == "1"):
                total1s +=1;


        if(total1s == n): return n;

        ans = 0;

        for i in range(n):
            if(A[i] == "0"):

                #  left side consecutive 1s calculation
                leftSideConsecutive1 = 0;
                for j in range(i-1, -1, -1):
                    if(A[j] == "1"):
                        leftSideConsecutive1 +=1;

                    else:
                        break;

                # right side consecutive 1s calculation

                rightSideConsecutive1 = 0;
                for j in range(i+1, n):
                    if(A[j] == "1"):
                        rightSideConsecutive1 +=1;

                    else:
                        break;
                l = leftSideConsecutive1;
                r = rightSideConsecutive1;
                count = l+r;

                if(total1s > (l+r)):
                    count +=1;


                ans = max(ans, count);


        return ans;