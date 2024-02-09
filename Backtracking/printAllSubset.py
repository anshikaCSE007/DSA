

# print All subset using backtracking approach  - 
#  questin link  -  https://www.codingninjas.com/studio/problems/print-all-subsets_2041995?leftPanelTabValue=SUBMISSION

# Problem Description
# Given a set of distinct integers A, return all possible subsets.

# NOTE:

# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# Also, the subsets should be sorted in ascending ( lexicographic ) order.
# The initial list is not necessarily sorted.


# Problem Constraints
# 1 <= |A| <= 16
# INTMIN <= A[i] <= INTMAX


# Input Format
# First and only argument of input contains a single integer array A.



# Output Format
# Return a vector of vectors denoting the answer.



# Example Input
# Input 1:

# A = [1]
# Input 2:

# A = [1, 2, 3]


# Example Output
# Output 1:

# [
#     []
#     [1]
# ]
# Output 2:

# [
#  []
#  [1]
#  [1, 2]
#  [1, 2, 3]
#  [1, 3]
#  [2]
#  [2, 3]
#  [3]
# ]


# Example Explanation
# Explanation 1:

#  You can see that these are all possible subsets.
# Explanation 2:

# You can see that these are all possible subsets.

#  -> Solution - 

class Solution:
	# @param A : list of integers
	# @return a list of list of integers
    
    def helpers(self, A, subset, n, i, res):
        if(i == n):
            res.append(subset.copy());
            # print(subset)
            return;
        # print(subset)
        # pick
        subset.append(A[i]);
        self.helpers(A,subset, n, i+1, res);

        # leave
        subset.pop();
        self.helpers(A, subset, n, i+1, res);


    def subsets(self, A):
        subset = [];
        res = []
        A.sort();
        self.helpers(A, subset, len(A), 0, res);
        return sorted(res);

    



# print All subset using backtracking approach  - 
#  questin link  -  https://www.codingninjas.com/studio/problems/print-all-subsets_2041995?leftPanelTabValue=SUBMISSION

# Solution - -> 

def helpers(n, arr, i, res = []):

    if(i == n):
        print((" ".join(map(str, res))));
        return;
    
    # take the ith element
    res.append(arr[i]);
    helpers(n, arr, i+1, res);

    # leave the ith element
    res.pop();
    helpers(n, arr, i+1, res);



def printAllSubsets(n, arr):
    # Write your code here.
    helpers(n, arr, 0);