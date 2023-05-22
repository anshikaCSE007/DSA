# problem statement - 
# https://www.interviewbit.com/problems/noble-integer/

class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
		A.sort();
		n = len(A);
		
		if(A[n-1] == 0):
			return 1;
		for i in range(n-1):
			
			if(A[i] != A[i+1]):
				if(A[i] == (n-1-i)):
					return 1;
					
		return -1;