
# Using Backtracking approach 
# Question link
# https://www.codingninjas.com/studio/problems/number-of-subsets_3952532?source=youtube&campaign=striver_dp_videos&utm_source=youtube&utm_medium=affiliate&utm_campaign=striver_dp_videos&leftPanelTabValue=PROBLEM

def helpers(arr, k, n, i, summ):
    if(i == n):
        if(summ == k):
            return 1;

        return 0;

    
    # take case 
    summ = summ + arr[i];
    x = helpers(arr, k, n, i+1, summ);

    # leave case
    summ = summ - arr[i];
    y = helpers(arr, k, n, i+1, summ);

    return x+y;

def findWays(arr, k: int) -> int:
    # Write your code here.
    return helpers(arr, k, len(arr), 0, 0);