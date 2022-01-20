class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        if not haystack: return -1
        
        needleNext = self.getNext(needle)
        
        j = 0
        for i in range(len(haystack)):
            while j > 0 and haystack[i] != needle[j]:
                j = needleNext[j - 1]
                
            if haystack[i] == needle[j]:
                if j == len(needle) - 1:
                    return i - j
                j += 1
                
        return -1
        
        
    def getNext(self, str):
        nxt = [0 for _ in range(len(str))]
        j = nxt[0]
        
        for i in range(1, len(str)):
            while j > 0 and str[i] != str[j]:
                j = nxt[j - 1]
            
            if str[i] == str[j]:
                nxt[i] = j + 1
                j += 1
                
        return nxt
        
        
        