
# Print All Permutations;
# Question link - https://leetcode.com/problems/permutations/


class Solution:
	# @param A : list of integers
	# @return a list of list of integers

    
    def solve(self, A, n, i, res):
        if(i == n):
            res.append(A.copy());
            return A;
        for j in range(i, n):
            A[i],A[j] = A[j],A[i];
            self.solve(A, n, i+1, res);
            A[i],A[j] = A[j],A[i];

            
    def permute(self, A):
        res = []
        n = len(A);
        self.solve(A, n, 0, res);
        return res;
