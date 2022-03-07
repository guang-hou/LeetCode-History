class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        
        def backtrack(startIndex):
            if sum(path) == target:
                res.append(path[:])
                return
            
            elif sum(path) < target and startIndex < len(candidates):
                for i in range(startIndex, len(candidates)):
                    if i > startIndex and candidates[i] == candidates[i - 1]:
                        continue
                    path.append(candidates[i])
                    backtrack(i + 1)
                    path.pop()
                    
        backtrack(0)
        
        return res
            