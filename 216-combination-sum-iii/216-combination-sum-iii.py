class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []
        
        def backtrack(k, n, startIndex):
            if sum(path) == n and len(path) == k:
                res.append(path[:])
                return
            elif len(path) < k:
	            for i in range(startIndex, 9 - (k - len(path) - 1) + 1):
	                path.append(i)
	                backtrack(k, n, i + 1)
	                path.pop()
                
        backtrack(k, n, 1)
        
        return res