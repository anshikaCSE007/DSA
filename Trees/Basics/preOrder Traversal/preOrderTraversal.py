

# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None

class Solution:
	# @param A : root node of tree
	# @return a list of integers
	def preorderTraversal(self, A):
		res = [];
		def traversal(node):
			if(node == -1 or not node):
				return;
			
			res.append(node.val);
			traversal(node.left);
			traversal(node.right);
        traversal(A)
		return res;