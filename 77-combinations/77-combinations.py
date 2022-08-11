class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.res, self.path = [], []
        
        for i in range(1, n + 1):
            self.backtrack(i, n, k)
        
        return self.res
        
    def backtrack(self, i, n, k):
        self.path.append(i)
        
        if len(self.path) == k:
            self.res.append(self.path[:])
            self.path.pop()
            return
        
        if len(self.path) + n - i < k:
            self.path.pop()
            return
        
        for j in range(i + 1, n + 1):
            self.backtrack(j, n, k)
        self.path.pop()
    