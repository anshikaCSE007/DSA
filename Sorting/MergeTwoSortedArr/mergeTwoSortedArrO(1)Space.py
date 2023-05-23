def merge(self,arr1,arr2,n,m):
    #code here
    i = len(arr1)-1;
    j = 0;
    while(i>=0 and j<len(arr2)):
        if(arr1[i] >= arr2[j]):
            arr1[i], arr2[j] = arr2[j], arr1[i];
            i-=1;
            j+=1;
        else:
            break;
    arr2.sort();
    arr1.sort();
    # arr2.sort();