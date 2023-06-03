

def changeToDepthTree(root, d=0):

    # Write your code here.
    if(root is None): return;
    root.data = d;
    changeToDepthTree(root.left, d+1);
    changeToDepthTree(root.right, d+1);
    pass
