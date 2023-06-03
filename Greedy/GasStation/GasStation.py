class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas);
        summ = 0;
        idx = 0;
        base = 0;
        temp = 0;

        if(sum(gas) < sum(cost)):
            return -1;

        for i in range(n):
           temp += (gas[i]);
           temp-=cost[i]
           if(temp < 0): 
               temp = 0;
               base = i+1;
            # break;


        return base