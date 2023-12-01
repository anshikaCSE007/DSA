def solve(self, A):
    if(A == 0):
        return 0;
    
    return A%10 + self.solve(A//10)