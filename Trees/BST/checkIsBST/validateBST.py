

# problem statement - https://leetcode.com/problems/validate-binary-search-tree/


class Solution:
    isValid = True;

    def isValidUtility(self, root):
        if(root is None):
            return (float('inf'), float('-inf'));

        l = self.isValidUtility(root.left);
        r = self.isValidUtility(root.right);

        if(l[1] >= root.val or r[0] <= root.val):
            print(l[1], r[0])
            self.isValid = False;

        return (min(root.val, l[0], r[0]), max(root.val, l[1], r[1]));


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValidUtility(root);
        return self.isValid;