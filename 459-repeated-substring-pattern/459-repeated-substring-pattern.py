class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        nxt = [0 for i in range(len(s))]
        j = nxt[0]  
        
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:  # j = nxt[i - 1]; s[j - 1] == s[i - 1]
                j = nxt[j - 1]
            
            if s[i] == s[j]:
                nxt[i] = j + 1
                j += 1
            else:
                nxt[i] = 0
                j = 0
               
        return nxt[len(s) - 1] > 0 and len(s) % (len(s) - nxt[len(s) - 1]) == 0
            
                