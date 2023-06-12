

# problem statement - https://leetcode.com/problems/search-in-a-binary-search-tree/description/



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if(root is None):
            return None;

        temp = root;


        while(temp):

            if(temp.val == val):
                return temp;

            elif(temp.val > val):
                temp = temp.left;

            else:
                temp = temp.right;

        
        return None;