
# https://www.geeksforgeeks.org/problems/equilibrium-point-1587115620/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

def equilibriumPoint(self,arr, n):
        # Your code here
        pf = [0]*n;
        pf[0] = arr[0]
        for i in range(1,n):
            pf[i] = pf[i-1]+arr[i];
            
        equiIdx = None;
        leftSumm = 0
        for i in range(n-1, -1, -1):
            if(i > 0):
                leftSumm = pf[i-1];
            else:
                leftSumm = 0;
            rightSumm = pf[n-1] - pf[i];
            
            if(leftSumm == rightSumm):
                equiIdx = i;
                
        if(equiIdx != None):
            return equiIdx+1;
            
        return -1;