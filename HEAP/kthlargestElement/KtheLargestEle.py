



# solution - 1 using min-heap - TC - O((n-k)logk)

import heapq;
class Solution:

	def kLargest(self,nums, n, k):
        res = nums[:k]
        heapq.heapify(res)
        
        for i in range(k, n):
            if nums[i] > res[0]:
                heapq.heappushpop(res, nums[i])
        
        return heapq.nlargest(k, res)


# solution - 2 - using QUICK_SELECT Algorithm--


import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        k = n - k
        while low <= high:
            pivotElement = nums[high]
            p1 = low
            p2 = high - 1

            while p1 <= p2:
                if nums[p1] < pivotElement:
                    p1 += 1
                elif nums[p2] > pivotElement:
                    p2 -= 1
                else:
                    nums[p1], nums[p2] = nums[p2], nums[p1]
                    p1 += 1
                    p2 -= 1

            nums[p1], nums[high] = nums[high], nums[p1]
            pivot = p1
            if pivot == k:
                return nums[pivot]
            elif pivot > k:
                high = pivot - 1
            else:
                low = pivot + 1

        return nums[k]

