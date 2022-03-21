class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not s: return 0
        
        g.sort()
        s.sort()
        res = 0
        
        for cookie in s[::-1]:
            for i in range(len(g) - 1, -1, -1):
                if cookie >= g[i]:
                    res += 1
                    g.pop(i)
                    break
        
        return res