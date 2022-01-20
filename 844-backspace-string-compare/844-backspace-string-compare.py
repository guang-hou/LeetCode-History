class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i, j = len(s) - 1, len(t) - 1
        
        sSkip, tSkip = 0, 0
        
        while True:
            while i > -1:
                if s[i] == '#':
                    sSkip += 1
                    i -= 1
                else:
                    if sSkip > 0:
                        i -= 1
                        sSkip -= 1
                    else:
                        break
                        
            while j > -1:
                if t[j] == '#':
                    tSkip += 1
                    j -= 1
                else:
                    if tSkip > 0:
                        j -= 1
                        tSkip -= 1
                    else:
                        break
            
            if i == -1 and j == -1: 
                return True
            elif i == -1 or j == -1:
                return False
            else:
                if s[i] != t[j]:
                    return False
                else:
                    i -= 1
                    j -= 1
        
        return True