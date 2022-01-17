class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        
        left, right = 0, len(s) - 1
        
        while s[left].isspace():
            left += 1
        while s[right].isspace():
            right -= 1
        
        s = s[left:right + 1]
        res = []
        
        for i in range(len(s)):
            if not s[i].isspace():
                res.append(s[i])
            else:
                if not s[i + 1].isspace():
                    res.append(s[i])
                else:
                    continue
        
        results = []
        tmp = []
        for i in range(len(res)):
            if not res[i].isspace() or i == len(s) - 1:
                tmp.append(res[i])
            else:
                results.append("".join(tmp))
                results.append(" ")
                tmp = []
                
        results.append("".join(tmp))
        results.reverse()
        
        return "".join(results)