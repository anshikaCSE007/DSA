# https://leetcode.com/problems/rectangle-overlap/
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        A = rec1[0];
        B = rec1[1];
        C = rec1[2];
        D = rec1[3];
        
        
        E = rec2[0];
        F = rec2[1];
        G = rec2[2];
        H = rec2[3];
        
        x1 = max(A,E);
        x2 = min(C,G);
        
        y1 = max(B,F);
        y2 = min(D, H);
        
        
        
        if(G<=A or E>=C or H<=B or F>=D):
            return 0;
        
        return (abs(x1-x2)*abs(y2-y1));
        