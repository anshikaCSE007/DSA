# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations);
        citations.sort();
        ans = 0;
        for i in range(n):
            noOfPublishedPapers = n-i;
            if(noOfPublishedPapers >= citations[i]):
                ans = citations[i];
            
            else:
                ans = max(ans,noOfPublishedPapers);

        
        return ans;