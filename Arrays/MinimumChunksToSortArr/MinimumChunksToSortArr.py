
# https://leetcode.com/problems/max-chunks-to-make-sorted/



class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr);
        leftMax = float("-inf");
        count = 0;
        
        for i in range(n):
            
            if(leftMax < arr[i]):
                leftMax = arr[i];
                
                
            if(leftMax == i):
                count+=1;
                
        return count;