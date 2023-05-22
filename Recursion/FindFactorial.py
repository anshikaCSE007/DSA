class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        if(A == 1 or A == 0):
            return 1;
        return self.solve(A-1)*A;