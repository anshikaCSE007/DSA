
class Solution:    
    #Complete this function
    def printNos(self,N):
        #Your code here
        if(N == 0):
            return;
        
        print(N, end=" ");
        self.printNos(N-1);
        

