
# problem statement - https://leetcode.com/problems/binary-tree-inorder-traversal/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recursiveCall(self, root, res):
        if(root is None):
            return;

        self.recursiveCall(root.left,res);
        res.append(root.val);
        self.recursiveCall(root.right,res);

        return res;

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [];
        return self.recursiveCall(root,res);