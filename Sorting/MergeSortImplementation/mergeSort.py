def merge(self, A, s, e, mid):
    n = (mid-s+1);
    m = (e-mid)
    B = [0]*n;
    C = [0]*m;
    for i in range(s,mid+1):
        B[i-s] = A[i];

    for i in range(mid+1, e+1):
        C[i-(mid+1)] = A[i];
    i = 0;
    j = 0;
    for k in range(s,e+1):
        if(i==n):
            A[k] = C[j];
            j+=1;
        
        elif(j==m or B[i] <= C[j]):
            A[k] = B[i];
            i+=1;
        
        else:
            A[k] = C[j];
            j+=1;




    def sort(self, A, s, e):
        if(s==e):
            return;

        mid = (s+e)//2;
        self.sort(A, s, mid);
        self.sort(A, mid+1, e);
        self.merge(A, s, e, mid);

    def solve(self, A):
        self.sort(A, 0, len(A)-1)
        return A;