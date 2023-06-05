

# problem statment - https://www.interviewbit.com/problems/vertical-order-traversal-of-binary-tree/


# Definition for a  binary tree node
# class TreeNode:
#	def __init__(self, x):
#		self.val = x
#		self.left = None
#		self.right = None
from collections import deque;
class Solution:
	# @param A : root node of tree
	# @return a list of list of integers
	def verticalOrderTraversal(self, A):
        queue = deque();
        queue.append([A, 0]);
        hm = {};
        minLevel = float('inf');
        maxLevel = float('-inf');
        res = [];
        while(len(queue)):
            x = queue.popleft();
            node = x[0];
            level = x[1];
            minLevel = min(minLevel, level);
            maxLevel = max(maxLevel, level);
            if(level in hm):
                hm[level].append(node.val);
            else:
                hm[level] = [node.val]
            if(node.left and node.left != -1):
                queue.append([node.left, level-1]);

            if(node.right and node.right != -1):
                queue.append([node.right, level+1]);
        
        for i in range(minLevel, maxLevel+1):
            res.append(hm[i]);

        return res;