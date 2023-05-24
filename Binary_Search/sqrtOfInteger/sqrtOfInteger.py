
# problem statement - https://leetcode.com/problems/sqrtx/description/
def sqrt(self, A):
    l=0;
    h=A;

    while(l<=h):
        mid = (l+h)//2;

        if(mid*mid <= A and (mid+1)*(mid+1) > A):
            return mid;
        
        elif(mid*mid > A):
            h = mid-1;
        
        else:
            l = mid+1;