

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# RECURSIVE SOLUTION

class Solution:
    def traversal(self, root, res):
        if(root is None):
            return;

        self.traversal(root.left, res);
        self.traversal(root.right, res);
        res.append(root.val);

        return res;


    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [];
        return self.traversal(root, res);

