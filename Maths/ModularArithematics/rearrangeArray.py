# problem statement - 
# https://www.interviewbit.com/problems/rearrange-array/

def arrange(self, A):
    n = len(A);
    
    # A[i] = A[i]*n;
    for i in range(n):
        A[i] = A[i]*n;

    for i in range(n):
        oldData = A[i]//n;
        # oldData is giving old A[i];
        # newData is giving A[A[i]]
        newData = A[oldData]//n;
        A[i] += newData;

    for i in range(n):
        A[i] = A[i]%n;

    return A[i];