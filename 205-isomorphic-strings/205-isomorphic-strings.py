class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        record1, record2 = {}, {}
        
        for i in range(len(s)):
            a , b = s[i], t[i]
            
            record1[a] = record1.get(a, b)
            record2[b] = record2.get(b, a)
            
            if record1[a] != b or record2[b] != a:
                return False
        
        return True