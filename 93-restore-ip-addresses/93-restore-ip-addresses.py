class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        path = []
        
        def backtrack(startIndex):
            if startIndex >= len(s) and len(path) == 4:
                res.append(".".join(path[:]))
            
            for i in range(startIndex, len(s)):
                first_part = s[startIndex : i + 1]
                if s[startIndex] == "0" and i > startIndex:
                    continue
                if int(first_part) <= 255 and int(first_part) >= 0:
                    path.append(first_part)
                    backtrack(i + 1)
                    path.pop()
            
        backtrack(0)
        
        return res