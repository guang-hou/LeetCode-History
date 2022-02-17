class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        
        def backtrack(start, end, k, n):
            if len(path) == k and sum(path) == n:
                res.append(path[:])
                return
            elif len(path) < k:
                for j in range(start, end - (k - len(path) - 1) + 1):
                    path.append(j)
                    backtrack(j + 1, end, k, n)
                    path.pop()
                
        backtrack(1, 9, k, n)
        
        return res