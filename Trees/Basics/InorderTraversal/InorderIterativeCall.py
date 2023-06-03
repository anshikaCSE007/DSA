
    def iterativeCall(self, root):
        curr = root;
        stack = []
        res = [];
        
        while(curr or len(stack)):
            if(curr is not None):
                stack.append(curr);
                curr = curr.left;

            else:
                curr = stack.pop();
                res.append(curr.val);
                curr = curr.right;

        return res;

        

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = [];
        # return self.recursiveCall(root,res);
        return self.iterativeCall(root);
