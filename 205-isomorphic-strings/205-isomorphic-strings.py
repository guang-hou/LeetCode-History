class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        record1, record2 = {}, {}
        
        for i in range(len(s)):
            a , b = s[i], t[i]
            if a not in record1:
                record1[a] = b
            else:
                if record1[a] != b:
                    return False
                
            if b not in record2:
                record2[b] = a
            else:
                if record2[b] != a:
                    return False
        
        return True