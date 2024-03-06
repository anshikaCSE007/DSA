


# https://leetcode.com/problems/bag-of-tokens/
class Solution:
    def bagOfTokensScore(self, token: List[int], power: int) -> int:
        token.sort();
        n = len(token);
        s = 0;
        p = power;
        maxS = 0
        i = 0;
        j = n-1;
        
        
        while(i<=j):
            
            if(p >= token[i]):
                p= p - token[i];
                s+=1;
                i+=1;
                
                if(maxS < s):
                    maxS = s;
                
            elif(s > 0):
                p+=token[j];
                s-=1;
                j-=1;
                
            else:
                return maxS;
            
            
        return maxS;