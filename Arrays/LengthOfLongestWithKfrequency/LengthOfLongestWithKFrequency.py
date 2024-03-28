

<!-- https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/ -->

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums);
        hm = {};
        i = 0;
        j = 0;
        l = 0;
        maxl = 1;
        while(i<=j and j<n):
            if(nums[j] in hm):
                if(hm[nums[j]] < k):
                    hm[nums[j]]+=1;

                else:
                    ele = nums[j];
                    while(i<j and nums[i]!=ele):
                        hm[nums[i]]-=1;
                        i+=1;
                    i+=1;
            elif(nums[j] not in hm):
                hm[nums[j]] = 1;
                
            l = (j-i+1);
            maxl = max(maxl, l);
            j+=1;
            
        
        return maxl;
                
                