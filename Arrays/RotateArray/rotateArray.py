

def rotate(nums, k) -> None:
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

print(rotate([1,2,3,4,5,6,7,8,9,10,55,66,77,88], 20))

def rotateUsingExtraSpace(nums, k):
    k = k%len(nums);
    l = len(nums);
    res = [0]*l;

    for i in range(l):
        if(i < k):
            res[i] = nums[l+i-k];
        
        else:
            res[i] = nums[i-k];

    
    return res;


print(rotateUsingExtraSpace([1,2,3,4,5,6,7,8,9,10,55,66,77,88], 20))

