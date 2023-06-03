
# problem statement - https://leetcode.com/problems/binary-tree-right-side-view/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if(root is None):
            return [];

        queue = deque([root]);
        last = root;
        res = [];
        while(len(queue)):
            temp = queue.popleft();

            if(temp.left):
                queue.append(temp.left);

            if(temp.right):
                queue.append(temp.right);


            if(temp == last):
                res.append(temp.val);
                if(len(queue)):
                    last = queue[-1];

        return res;