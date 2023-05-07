# problem statement - https://leetcode.com/problems/insert-interval/description/

# TC - O(n);
# SC - O(1)  neglecting output array;

def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals);
        res = [];
        l = newInterval[0];
        r = newInterval[1];
        t = 0;
        for i in range(t,len(intervals)):
            si = intervals[i][0];
            ei = intervals[i][1];
            # print((l > ei or r < si),l,ei,r,si)
            if(not (l > ei or r < si)):
                l = min(l, si);
                r = max(r, ei);
                # print(l, r)

            else:
                if(l > ei):
                    res.append([si, ei]);
                elif(r < si):
                    res.append([l, r]);
                    r = ei;
                    l = si;


        res.append([l, r]);

        return res;