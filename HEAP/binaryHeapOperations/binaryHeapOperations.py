

#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''
#Function to insert a value in Heap.
def insertKey (x):
    global curr_size;
    heap[curr_size] = x;
    # print(heap, 'here')
    curr_size+=1
    idx = curr_size-1;
    parIdx = (idx-1)//2;
    
    while(idx!=0 and heap[idx] < heap[parIdx]):
        heap[idx], heap[parIdx] = heap[parIdx], heap[idx];
        idx = parIdx;
        parIdx = (idx-1)//2;
    
    # print(heap, 'insert')
    # print(curr_size, 'curr size')
    return heap;
    
    
    

#Function to delete a key at ith index.
def deleteKey (i):
    global curr_size
    if(curr_size <= i):
        return None;
        
    idx = curr_size-1;
    heap[i], heap[idx] = heap[idx], heap[i];
    # print(idx, i, 'indd')
    heap[idx] = 0;
    curr_size -=1;
    idx = i;
    left = (2*idx +1);
    right = (2*idx + 2);
    n = curr_size;
    while(idx < n and ((left < n and heap[idx] > heap[left]) or (right < n and heap[idx] > heap[right]))):
        if(right >= n or heap[left] <= heap[right]):
            heap[idx], heap[left] = heap[left], heap[idx];
            idx = left;
        
        else:
            heap[idx], heap[right] = heap[right], heap[idx];
            idx = right;
    
        
        left = (2*idx +1);
        right = (2*idx + 2);
    
    
    
    idx = i;
    parIdx = (idx-1)//2;
    
    while(idx!=0 and idx < n and heap[parIdx] > heap[idx]):
        heap[parIdx], heap[idx] = heap[idx], heap[parIdx];
        temp = idx;
        idx = parIdx;
        parIdx = (idx-1)//2;
        
    # print(heap, 'delete')
    # print(curr_size, 'curr size')
        
    
#Function to extract minimum value in heap and then to store 
#next minimum value at first index.
def extractMin ():
    global curr_size
    if(curr_size <= 0):
        return -1;
    n = curr_size;
    ans = heap[0];
    # print(n, 'idx')
    heap[0] = heap[n-1];
    
    heap[n-1] = 0;
    # print(heap, 'extraxt')
    curr_size-=1;
    n = curr_size;
    idx = 0;
    left = (2*idx + 1);
    right = (2*idx + 2);
    while(idx < n and ((left < n and heap[idx] > heap[left]) or (right < n and heap[idx] > heap[right]))):
        if(right >= n or heap[left] <= heap[right]):
            heap[idx], heap[left] = heap[left], heap[idx];
            idx = left;
        
        else:
            heap[idx], heap[right] = heap[right], heap[idx];
            idx = right;
    
        
        left = (2*idx +1);
        right = (2*idx + 2);
    # print(heap, 'extraxt')
    # print(curr_size, 'curr size')
        
    return ans;