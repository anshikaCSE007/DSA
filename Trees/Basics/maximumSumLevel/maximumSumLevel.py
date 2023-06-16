
# problem statment - https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/
from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root]);
        last = root;
        ans = 0;
        level = 1;
        summ = 0;
        maxSum = float('-inf');

        while(len(queue)):
            node = queue.popleft();
            summ+=node.val;
            if(node.left):
                queue.append(node.left);

            if(node.right):
                queue.append(node.right);

            
            if(node == last):
                if(len(queue)):
                    last = queue[-1];
                if(maxSum < summ):
                    maxSum = summ;
                    ans = level;
                level +=1;
                summ = 0;


            
        
        return ans;