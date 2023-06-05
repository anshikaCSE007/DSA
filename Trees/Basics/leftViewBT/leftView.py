
# problem statement - https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article

from collections import deque


def LeftView(root):
    
    # code here
    if(root is None):
        return [];
        
    res = [root.data];
    last = root;
    queue = deque([root]);
    
    while(len(queue)):
        
        temp = queue.popleft();
        
        if(temp.left):
            queue.append(temp.left);
        
        if(temp.right):
            queue.append(temp.right);
            
            
        if(temp == last and len(queue)):
            res.append(queue[0].data);
            last = queue[-1];
                
    
    return res;