

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        k = k%len(nums);
        for i in range(len(nums)//2):
            nums[i], nums[len(nums)-i-1] = nums[len(nums)-i-1], nums[i];
        
        print(nums)

        for i in range(k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i];
        print(nums)
        j = len(nums)-1
        i = k
        while(i<=j):
            nums[i], nums[j] = nums[j], nums[i];
            i+=1;
            j-=1;


        print(nums)
        return nums;
