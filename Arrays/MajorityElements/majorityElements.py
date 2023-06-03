

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # 0 1 2 3 4 5 6 7 8 9 10 11
        # 2 2 1 1 3 1 3 3 3 3 4 3

        c = 1;
        ele = nums[0];


        for i in range(1, len(nums)):
            if(nums[i] == ele):
                c +=1;
            
            else:
                c-=1;

            if(c == 0):
                c = 1;
                ele = nums[i];

        return ele;