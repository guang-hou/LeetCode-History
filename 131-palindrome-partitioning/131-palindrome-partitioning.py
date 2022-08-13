class Solution:
    def __init__(self):
        self.path = []
        self.res = []
    
    def partition(self, s: str) -> List[List[str]]:
        self.dfs(s, 0)
        
        return self.res
        
        
    def dfs(self, s, nodeStartIndex):
        if nodeStartIndex == len(s):
            self.res.append(self.path[:])
            return        
        
        for i in range(nodeStartIndex, len(s)):
            if self.isParlindrome(s, nodeStartIndex, i + 1):
                self.path.append(s[nodeStartIndex:i + 1])
                self.dfs(s, i + 1)
                self.path.pop()
            
    # Check if s[start:end] is a parlindrome, not including s[end]
    def isParlindrome(self, s, start, end):
        end -= 1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        
        return True
        