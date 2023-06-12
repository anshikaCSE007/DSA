

# problem statment - https://leetcode.com/problems/maximum-value-at-a-given-index-in-a-bounded-array/description/


class Solution:

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        eleLeft = index;
        eleRight = n - index-1;

        l = 1;
        h = maxSum;
        ans = 0;
        ans = 0;
        while(l <= h):
            mid = (l+h)//2;

            leftSum = 0;
            rightSum = 0;

            maxx = mid;
            ele = mid-1;
            # calculation of left sum

            # when no extra 1s will be there.
            if(eleLeft <= ele):
                leftSum = (eleLeft)*(ele + (ele-eleLeft+1))
                leftSum = leftSum//2
            # when 1s are there
            elif(eleLeft > ele):
                x = ele;
                leftSum = (x*(x+1))//2;
                leftSum += (eleLeft-ele);

            # calculation of rightSum

            # when no extra 1s will be there.
            if(eleRight <= ele):
                rightSum = (eleRight)*(ele + (ele-eleRight+1))
                rightSum = rightSum//2

            else:
                x = ele;
                rightSum = (x*(x+1))//2;
                rightSum += (eleRight-ele);
            totalSum = maxx+leftSum+rightSum;
            
            if(totalSum == maxSum):
                ans= maxx;
                l = mid+1;

            elif(totalSum > maxSum):
                h = mid-1;

            else:
                ans = maxx;
                l = mid+1;

        
        return ans;