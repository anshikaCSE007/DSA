


#User function Template for python3

# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

from collections import deque
class Solution:
    
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        queue = deque([(root,0)]);
        hm = { 0: root }
        factor = 0;
        
        while(len(queue)):
            x = queue.popleft();

            # we can also calculate minIdx and maxIdx in this loop itself
            # minIdx = min(minIdx, x[1]);
            # maxIdx = max(maxIdx, x[1]);
            
            if(x[0].left):
                leftFact = x[1]-1;
                queue.append((x[0].left, leftFact));
                if(leftFact not in hm):
                    hm[leftFact] = x[0].left;
                
                
                
            if(x[0].right):
                
                rightFact = x[1]+1;
                queue.append((x[0].right, rightFact));
                if(rightFact not in hm):
                    hm[rightFact] = x[0].right;
                    
                    
        
        minIdx = 0;
        maxIdx = 0;
        
        for key, val in hm.items():
            minIdx = min(minIdx, key);
            maxIdx = max(maxIdx, key);
            
            
        res = [];
        
        for i in range(minIdx, maxIdx+1):
            res.append(hm[i].data);
            
            
        return res;