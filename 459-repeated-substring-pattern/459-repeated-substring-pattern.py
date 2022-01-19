class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        nxt = [-1 for i in range(len(s))]
        j = nxt[0]
        
        for i in range(1, len(s)):
            while j > -1 and s[i] != s[j + 1]:
                j = nxt[j]
            
            if s[i] == s[j + 1]:
                nxt[i] = j + 1
                j += 1
            else:
                nxt[i] = -1
                j = -1
               
        return nxt[len(s) - 1] > -1 and len(s) % (len(s) - (nxt[len(s) - 1] + 1)) == 0
            
                