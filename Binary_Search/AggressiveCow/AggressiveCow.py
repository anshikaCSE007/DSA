

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer

    def checkIfAllCowsPlaced(self, dist, A, B):
        n = len(A);
        c = 1
        last = A[0]

        for i in range(1, n):
            if((A[i] - last) >= dist):
                c +=1;
                last = A[i]
        
        return c;

    def solve(self, A, B):
        A.sort();
        l = 1;
        h = A[len(A)-1]-A[0];
        ans  = 0;

        while(l <= h):
            mid = (l+h)//2;
            count = self.checkIfAllCowsPlaced(mid, A, B);
            if(count >= B):
                ans = mid;
                l = mid+1;

            else:
                h = mid-1;
        
        return ans;