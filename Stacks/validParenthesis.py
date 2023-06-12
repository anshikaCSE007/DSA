

# problem statment -  https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

class Solution:
    def isValid(self, s: str) -> bool:
        openBracs = {'[', '{', '('};
        closeBracs = {']': '[', '}': '{', ')': '('};
        n = len(s);
        stack = [];

        for i in range(n):
            if(s[i] in openBracs):
                stack.append(s[i]);

            elif(len(stack) and  (s[i] in closeBracs) and (stack[-1] == closeBracs[s[i]])):
                stack.pop();

            else:
                return False;

        
        return bool(not len(stack))