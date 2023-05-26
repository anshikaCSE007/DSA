

def longestConsecutive(self, A):
		n = len(A);
		setA = set(A);
		ans = 0;
		l = 0
		for i in range(n):
			x = A[i]-1;

			if(x not in setA):
				l = 0;
				y = A[i];
				while(y in setA):
					l+=1;
					y=y+1;

			ans = max(ans, l);
		
		return ans;