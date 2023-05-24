

    def searchMatrix(self, A, B):
        n = len(A);
        m = len(A[0]);

        # choose row no using BS;

        l = 0;
        h = n-1;
        row = 0;

        while(l<=h):

            mid = (l+h)//2;

            if(A[mid][m-1] == B):
                return 1;

            elif(A[mid][m-1] > B):
                row = mid;
                h = mid-1;

            else:
                l = mid+1;

        l = 0;
        h = m-1
        while(l<=h):

            mid = (l+h)//2;

            if(A[row][mid] == B):
                return 1;

            elif(A[row][mid] > B):
                h = mid-1;

            else:
                l = mid+1;

        
        return 0;