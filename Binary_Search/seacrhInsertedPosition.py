# problem statement - https://leetcode.com/problems/search-insert-position/description/

def searchInsert(self, nums: List[int], target: int) -> int:
    l = 0;
    h = len(nums)-1;
    m = 0;

    while(l<=h):
        m = (l+h)//2;

        if(nums[m] == target):
            return m;

        elif(nums[m] < target):
            l = m+1;

        else:
            h = m-1;

    return h+1;