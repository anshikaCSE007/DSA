


# problem statement - https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def buildTreeUtility(self, inorder, postorder, s_in, e_in, s_p, e_p):
        
        if(s_in > e_in or s_p > e_p):
            return None;


        rootData = postorder[e_p];
        idx = s_in;
        root = TreeNode(rootData);
        for i in range(s_in, e_in+1):
            if(inorder[i] == rootData):
                idx = i;
                break;

        
        countLeft = idx - s_in;
        countRight = e_in - idx;

        root.left = self.buildTreeUtility(inorder, postorder, s_in, idx-1, s_p, e_p-countRight-1);
        root.right = self.buildTreeUtility(inorder, postorder, idx+1, e_in, s_p + countLeft, e_p-1);

        return root;

        # countLeft+1---->e_p-1



    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if(len(inorder) == 0):
            return None;

        s_in = 0;
        e_in = len(inorder)-1;
        s_p = 0;
        e_p = e_in;
        return self.buildTreeUtility(inorder, postorder, s_in, e_in, s_p, e_p);