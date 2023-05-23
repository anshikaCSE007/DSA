def sortColors(self, A):
    l = 0;
    m = 0;
    h = len(A)-1;

    while(m<=h):
        if(A[m]==0):
            A[m],A[l] = A[l],A[m];
            m+=1;
            l+=1;

        elif(A[m]==1):
            m+=1;

        else:
            A[m],A[h] = A[h],A[m];
            h-=1;

    return A;
