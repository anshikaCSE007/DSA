

# problem statment - https://www.codingninjas.com/codestudio/problems/floor-from-bst_920457


# iterative 

def floorInBST(root, X):
    # Write your Code here.
    temp = root;
    ans = None;
    while(temp):
        if(temp.data == X):
            return temp.data;

        elif(temp.data > X):
            temp = temp.left;

        else:
            ans = temp.data;
            temp = temp.right;

    return ans;