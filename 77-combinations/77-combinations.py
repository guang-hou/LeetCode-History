class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, path = [], []
        
        for i in range(1, n + 1):
            self.backtrack(i, n, k, path, res)
        
        return res
        
    def backtrack(self, i, n, k, path, res):
        path.append(i)
        
        if len(path) == k:
            res.append(path[:])
            path.pop()
            return
        
        for j in range(i + 1, n + 1):
            self.backtrack(j, n, k, path, res)
        path.pop()
    