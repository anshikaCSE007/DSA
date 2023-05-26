class Solution:
	# @param A : integer
	# @param B : integer
	# @param C : list of integers
	# @return an integer
	def numberOfPaintersInT(self, t, boards, unitTime):
		count = 1;
		time = t;
		for i in range(len(boards)):
			if(boards[i]*unitTime > t):
				return -1;
			
			if(boards[i]*unitTime <= time):
				time = time - (boards[i]*unitTime);
		
			else:
				time = t - (boards[i]*unitTime);
				count+=1;
		
		return count;
		
				
	def paint(self, A, B, C):
        ans = max(C)*B;
		l = max(C)*B;
		h = (sum(C))*B;
		while(l<=h):
			mid = (l+h)//2;
			calP = self.numberOfPaintersInT(mid, C, B);
			calPMidLess1 = self.numberOfPaintersInT(mid-1, C, B);
			# print(calP, calPMidLess1)
			if(calP == -1):
				l = mid+1;
			if(calP > 0 and calP <= A and calPMidLess1 > A):
				return mid%10000003;
			
			elif(calP > A):
				l = mid+1;

			else:
				h = mid-1;
		
		return ans%10000003;