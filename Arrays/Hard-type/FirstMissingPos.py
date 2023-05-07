# problem statement - https://leetcode.com/problems/first-missing-positive/description/

def firstMissingPositive(self, A: List[int]) -> int:
        n = len(A);

        # looping
        i = 0;

        for i in range(n):
            
            while(A[i] > 0 and A[i] <= n and A[i] != i+1):
                element = A[i];
                correctIdx = A[i]-1;
                temp = A[correctIdx];
                A[correctIdx] = element;
                A[i] = temp;
                if(element == temp):
                    break;
        
        for i in range(n):
            if(A[i] != i+1):
                return i+1;

        return n+1;

  # TC - O(n). -> maximum number of swaps - n only
  # SC - O(1)