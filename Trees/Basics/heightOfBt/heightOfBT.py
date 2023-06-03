

import sys;
sys.setrecursionlimit(10 ** 6)
class Solution:
    # @param A : root node of tree
    # @return an integer
    def solve(self, A):

        if(A is None):
            return 0;

        return 1 + max(self.solve(A.left), self.solve(A.right));