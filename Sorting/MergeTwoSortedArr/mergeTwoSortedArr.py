
def solve(self, A, B):
    lenA = len(A);
    lenB = len(B);
    tl = lenA + lenB
    sortedArr = [0]*tl;
    i = 0;
    j = 0;
    # print(sortedArr)
    for k in range(0,(lenA+lenB)):
        if(i==lenA):
            sortedArr[k] = B[j];
            j+=1;
        
        elif((j==lenB) or (A[i]<=B[j])):
            sortedArr[k] = A[i];
            i+=1
        
        else:
            sortedArr[k] = B[j];
            j+=1;
    # print
    return sortedArr;