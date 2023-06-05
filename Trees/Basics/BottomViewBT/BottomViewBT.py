
# problem statement - https://practice.geeksforgeeks.org/problems/bottom-view-of-binary-tree/1

from collections import deque
class Solution:
    def bottomView(self, root):
        # code here
        queue = deque([(root, 0)]);
        
        hm = {0: root};
        maxIdx = 0;
        minIdx = 0;
        while(len(queue)):
            x = queue.popleft();
            level = x[1]
            maxIdx = max(maxIdx, level);
            minIdx = min(minIdx, level);
            if(x[0].left):
                queue.append((x[0].left, level-1));
                hm[level-1] = x[0].left;
                
            if(x[0].right):
                queue.append((x[0].right, level+1));
                hm[level+1] = x[0].right;
                
                
        
        res = [];
        
        for i in range(minIdx, maxIdx+1):
            res.append(hm[i].data);
            
            
        return res;