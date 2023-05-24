

def gcd(self, A, B):
    if(B==0):
        return A;
    
    return self.gcd(B, A%B);

def solve(self, A, B, C):
    lcm = (C*B)//self.gcd(B,C);
    l=min(B,C);
    h=l*A;

    while(l<=h):
        mid = (l+h)//2;
        count = (mid//B) + (mid//C) - (mid//lcm)

        if(count==A and (mid%B == 0 or mid%C == 0)):
            return mid%(10**9 + 7);

        elif(count>=A):
            h = mid-1;

        else:
            l = mid+1;