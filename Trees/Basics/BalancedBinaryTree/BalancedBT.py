


# problem statement - https://leetcode.com/problems/balanced-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    isBalance = True;

    def checkHeight(self, root):
        if(root is None):
            return -1;

        leftHeight = self.checkHeight(root.left);
        rightHeight = self.checkHeight(root.right);

        height = 1 + max(leftHeight, rightHeight);

        if(abs(leftHeight - rightHeight) > 1):
            self.isBalance = False;

        return height;

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.checkHeight(root);

        return self.isBalance;