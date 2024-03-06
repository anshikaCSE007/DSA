
# 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits);
        
        digits[n-1] = digits[n-1]+1;
        
        carry = 0;
        res = [];
        for i in range(n-1, -1, -1):
            k = digits[i]+carry;
            ele = k%10;
            carry = k//10;
            
            res.append(ele);
            
            
        p = res[-1];
        if(carry > 0):
            res[-1] = p%10;
            res.append(carry);
            
        i = 0;
        j = len(res)-1;
        
        while(i<=j):
            res[i], res[j] = res[j], res[i];
            i+=1;
            j-=1;
            
            
        return res;
            