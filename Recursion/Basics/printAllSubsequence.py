string = str(input());

def printAllSS(ind, res, arr, n):
    if(ind >= n):
        print(''.join(res));
        return;

    res.append(arr[ind]);
    printAllSS(ind+1, res, arr, n);
    res.pop();
    printAllSS(ind+1, res, arr, n);

printAllSS(0, [], string, len(string));