#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
		# code here
		max1 = float("-inf");
		max2 = float("-inf");
		
		for i in range(n):
		    if(arr[i] > max1 and arr[i] > max2):
		        max2 = max1;
		        max1 = arr[i];
		        
		    elif(arr[i] > max2 and arr[i] < max1):
		        max2 = arr[i];
		    
		  #  print(max1, max2)
        
        if(max2 != float("-inf")):
            return max2;
            
        return -1;
		        
	   