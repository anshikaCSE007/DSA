# https://www.geeksforgeeks.org/problems/faulty-wiring-and-bulbs2939/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

class Solution:
    def countFlips(self,arr,n):
        #code here
        n = len(arr);
        count = 0;

        for i in range(n):
            if(count%2 == 1):
                currState = 1 - arr[i];

            else:
                currState = arr[i];
            
            if(currState==0):
                count+=1;

        return count;