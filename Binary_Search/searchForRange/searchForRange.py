


 def searchRange(self, A, B):
      noOfEle = len(A);
      l = 0;
      r = noOfEle-1;

      leftIdx = -1;
      rightIdx = -1;

      while(l<=r):
          mid = (l+r)//2;
          
          if(A[mid] == B):
              leftIdx = mid;
              r = mid-1;
          
          if(A[mid] >= B):
              r = mid-1;
          
          else:
              l = mid+1;
      
      l = 0;
      r = noOfEle-1;
      while(l<=r):
          mid = (l+r)//2;
          
          if(A[mid] == B):
              rightIdx = mid;
              l = mid+1;
          
          if(A[mid] <= B):
              l = mid+1;
          
          else:
              r = mid-1;

      return [leftIdx, rightIdx]