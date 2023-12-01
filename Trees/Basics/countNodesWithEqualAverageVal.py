
# https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/description/?envType=daily-question&envId=2023-11-02
# 2265. Count Nodes Equal to Average of Subtree
# Solved
# Medium
# Topics
# Companies
# Hint
# Given the root of a binary tree, return the number of nodes where the value of the node is equal to the average of the values in its subtree.

# Note:

# The average of n elements is the sum of the n elements divided by n and rounded down to the nearest integer.
# A subtree of root is a tree consisting of root and all of its descendants.
 

# Example 1:


# Input: root = [4,8,5,0,1,null,6]
# Output: 5
# Explanation: 
# For the node with value 4: The average of its subtree is (4 + 8 + 5 + 0 + 1 + 6) / 6 = 24 / 6 = 4.
# For the node with value 5: The average of its subtree is (5 + 6) / 2 = 11 / 2 = 5.
# For the node with value 0: The average of its subtree is 0 / 1 = 0.
# For the node with value 1: The average of its subtree is 1 / 1 = 1.
# For the node with value 6: The average of its subtree is 6 / 1 = 6.



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    count = 0;
    def helpersFunc(self, root):
        if(root == None):
            return [0,0];

        left = self.helpersFunc(root.left);
        right = self.helpersFunc(root.right);
        leftH = left[0];
        leftS = left[1];
        rightH = right[0];
        rightS = right[1];
        totalSum = leftS+rightS+root.val;
        average = (totalSum)//(leftH + rightH + 1);
        if(average == root.val):
            self.count+=1;

        return [leftH+rightH+1, totalSum];
        
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.helpersFunc(root);
        return self.count;