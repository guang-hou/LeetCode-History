class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        
        def backtrack(i, n, k):

            if len(path) == k:
                res.append(path[:])
                return
            
            for j in range(i, n + 1):
                path.append(j)
                backtrack(j + 1, n, k)
                path.pop()
        
        backtrack(1, n, k)
        
        return res