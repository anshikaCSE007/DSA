class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        hashMap = {};
        lenA = len(A);
        minLength = float('inf');

        for i in range(lenA):
            if(A[i] in hashMap):
                minLength = min(minLength, i-hashMap[A[i]]);
            
            hashMap[A[i]] = i;
        if(len(hashMap) == lenA):
            return -1;
        return minLength;
