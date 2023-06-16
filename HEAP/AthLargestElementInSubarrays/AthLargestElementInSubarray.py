


import heapq;
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        n = len(B);
        temp = [];
        res = []

        for i in range(n):
            if(i<A-1):
                heapq.heappush(temp, B[i]);
                res.append(-1);

            elif(i==A-1):
                heapq.heappush(temp, B[i]);
                res.append(temp[0]);

            else:
                heapq.heappushpop(temp, B[i])
                res.append(temp[0]);

        
        return res;

        