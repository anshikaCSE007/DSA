
class Solution:
    def findPeakElement(self, A: List[int]) -> int:
        n = len(A);
        l = 0;
        h = n-1;



        while(l<=h):
            mid = (l+h)//2;

            if((mid == 0 or (A[mid] > A[mid-1])) and (mid == n-1 or (A[mid] > A[mid+1]))):
                return mid;
            
            elif(mid == 0 or A[mid] > A[mid-1]):
                l = mid+1;

            else:
                h = mid-1;
