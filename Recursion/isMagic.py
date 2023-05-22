class Solution:
    # @param A : integer
    # @return an integer
    def sumDigits(self, B):
        if(B == 0):
            return 0;
        return B%10 + self.sumDigits(B//10);
    def solve(self, A):
        while(A > 9):
            A = self.sumDigits(A);
        if(A == 1):
            return 1;
        else:
            return 0;