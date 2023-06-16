

# problem statment - https://leetcode.com/problems/find-median-from-data-stream/description/

import heapq;
class MedianFinder:

    def __init__(self):
        self.maxHeap = [];
        self.minHeap = [];
        

    def addNum(self, num: int) -> None:
        # first just insert the number satisfying the conditions
        if(not len(self.maxHeap) or num < -self.maxHeap[0]):
            heapq.heappush(self.maxHeap, -1*num);
        else:
            heapq.heappush(self.minHeap, num);

        leftSize = len(self.maxHeap);
        rightSize = len(self.minHeap);

        # modify if size condition not satisfied
        if(rightSize > leftSize):
            heapq.heappush(self.maxHeap, -1*heapq.heappop(self.minHeap));

        elif(leftSize-rightSize > 1):
            heapq.heappush(self.minHeap, -1*heapq.heappop(self.maxHeap));

        
        

    def findMedian(self) -> float:
        size = len(self.maxHeap) + len(self.minHeap);
        ans = 0;
        if(not len(self.minHeap)):
            return -self.maxHeap[0];

        if(size%2!=0):
            ans =  -self.maxHeap[0];

        elif(size%2 == 0):
            ans = (-1*self.maxHeap[0] + self.minHeap[0])/2;
        

        
        return ans;
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()