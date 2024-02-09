
def generateNums(n, i, arr):
    if(i==n):
        print(''.join(str(x) for x in arr));
        return;

    arr[i] = 1;
    generateNums(n, i+1, arr);
    arr[i] = 2;
    generateNums(n, i+1, arr);


n = int(input());
arr = [0]*n;
print(generateNums(n, 0, arr));


