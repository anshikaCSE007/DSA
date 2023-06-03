

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def postorderTraversal(self, A):
        stack = [];
        curr = A;
        res = [];

        while(curr or len(stack)):
            if(curr is not None):
                stack.append(curr);
                curr = curr.left;

            else:
                temp = stack[-1].right;

                if(temp is None):
                    

                    temp = stack[-1];
                    res.append(temp.val);
                    stack.pop();

                    while(len(stack) and temp == stack[-1].right):
                        temp  = stack.pop();
                        res.append(temp.val);

                else:
                    curr = temp;

        return res;