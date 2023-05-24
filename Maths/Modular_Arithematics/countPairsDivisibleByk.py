# Problem statement - 
# https://practice.geeksforgeeks.org/problems/count-pairs-in-array-divisible-by-k/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article


def countKdivPairs(self, arr, n, k):
        #code here
        n = len(arr);
        pairs = 0;
        freqArr = [0]*(k);

        for i in range(len(arr)):
            idx = (arr[i]%k);
            freqArr[idx] +=1;

        x = freqArr[0];
        pairs += ((x*(x-1))//2);

        if(k%2 == 0):
            x = freqArr[k//2];
            pairs += ((x*(x-1))//2);

        
        i = 1;
        j = k-1;
        while(i <j):
            x = freqArr[i];
            y = freqArr[j]; 
            pairs += (x*y);
            i +=1;
            j -=1;
        return pairs;