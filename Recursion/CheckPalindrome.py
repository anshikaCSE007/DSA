class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A, s, e):
        if(s>e):
            return True;
        if(A[s] != A[e]):
            return False;
        
        return self.isPalindrome(A, s+1, e-1);

    def solve(self, A):
        if(self.isPalindrome(A, 0, len(A)-1)):
            return 1;
        return 0;