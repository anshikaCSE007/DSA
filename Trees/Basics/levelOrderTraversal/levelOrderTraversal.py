


# problem statement - https://leetcode.com/problems/binary-tree-level-order-traversal/
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(root is None):
            return;
        queue = deque();
        queue.append(root)
        last = root;
        level = [];
        ans = [];
        while(len(queue)):
            temp = queue.popleft();
            print(temp.val)
            level.append(temp.val);

            if(temp.left is not None):
                queue.append(temp.left);

            if(temp.right is not None):
                queue.append(temp.right);

            if(temp == last):
                ans.append(level);
                
                if(len(queue)):
                    last = queue[-1];
                    level = [];

        return ans;