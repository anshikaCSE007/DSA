class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        vowels = set(["a", "e", "i", "o","u", "A", "E", "I", "O", "U"]);
        
        count = 0;
        A = list(A);
        n = len(A);
        for i in range(len(A)):
            if(A[i] in vowels):
                alphas = (n-i);
                count+=alphas;
                
                
        return (count%10003);