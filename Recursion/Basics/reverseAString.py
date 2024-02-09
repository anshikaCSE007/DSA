class Solution:
    
    def helpers(self, s, e, word):
        if(s>=e):
            return word;
            
        temp = word[s];
        word[s] = word[e];
        word[e] = temp;
        self.helpers(s+1, e-1, word);

    
    def reverseWord(self, str: str) -> str:
        #your code here
        self.helpers(0, len(str)-1, str);
        return str;