# problem statement - https://leetcode.com/problems/find-peak-element/description/

class Solution:
    def singleNonDuplicate(self, A: List[int]) -> int:
        n = len(A);

        l = 0;
        h = n-1;

        while(l<=h):
            mid=(l+h)//2;

            if((mid==0 or A[mid] != A[mid-1]) and (mid==n-1 or A[mid] != A[mid+1])):
                return A[mid];

            elif((mid==0 or A[mid] == A[mid-1])):
                if(mid%2 == 0):
                    h = mid-1;
                else:
                    l = mid + 1;
                    

            elif((mid==n-1 or A[mid] == A[mid+1])):
                if(mid%2 == 0):
                    l = mid+1;
                else:
                    h = mid - 1;

        return ans;