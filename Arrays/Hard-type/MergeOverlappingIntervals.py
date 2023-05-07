# problem statement - https://leetcode.com/problems/merge-intervals/description/



# check if si lies in range of [ l ----- r ]
# as intervals are sorted with first element thats for sure si<= l;
# so just need to check for si is overlapping with l --- r or not  
# overlapping cases: 
# case 1: 
# l----------r 
#      si---------ei  
#  new interval -  l--------ei
# case 2 : 
#     l------------r
#        si------ei 
# new interval - l--------r; 

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort();
        n = len(intervals);
        l = intervals[0][0];
        r = intervals[0][1];
        res = [];

        for i in range(1, n):
            si = intervals[i][0];
            ei = intervals[i][1];
            
            if(si <= r):
                # overlapping
                r = max(r, ei);
            
            else:
                # non overlapping
                res.append([l, r]);
                l = si;
                r = ei;

        res.append([l, r]);

        return res;