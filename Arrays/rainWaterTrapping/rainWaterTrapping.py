


class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height);
        rightMax = [0]*n;
        rightMax[n-1] = height[n-1];
    
        
        totalArea = 0
        for i in range(n-2, -1 ,-1):
            rightMax[i] = max(rightMax[i+1], height[i]);
            
        leftMax = 0
        
        for i in range(n):
            factor = min(leftMax, rightMax[i]);
            
            if(factor >= height[i]):
                totalArea += (factor-height[i]);
                
            leftMax = max(leftMax, height[i]);
        
        return totalArea;