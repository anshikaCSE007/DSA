class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @return an integer
    def pow(self, A, B, C):
        if(B == 0):
            return 1%C;
        p = self.pow(A, B//2, C);
        if(B%2 ==0 ):
            return (p*p)%C;
        else:
            return (((p*p)%C) *A)%C