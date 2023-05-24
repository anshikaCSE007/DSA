
# problem statement - https://leetcode.com/problems/search-in-rotated-sorted-array/description/
class Solution:
    def search(self, A: List[int], target: int) -> int:
        n = len(A);

        l = 0;
        h = n-1;

        while(l<=h):
            mid = (l+h)//2;

            if(A[mid] == target):
                return mid;

            if(target >= A[0]):
                if(A[mid] < A[0]):
                    h = mid-1;

                elif(A[mid] >= A[0]):
                    if(target > A[mid]):
                        l=mid+1;

                    else:
                        h=mid-1;
            
            elif(target < A[0]):
                if(A[mid] >= A[0]):
                    l = mid+1;

                elif(A[mid] < A[0]):
                    if(target > A[mid]):
                        l=mid+1;

                    else:
                        h=mid-1;

        return -1;
                