class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []
        
        def backtrack(startIndex, currentTarget):
            if currentTarget == 0:
                res.append(path[:])
                return
            
            elif currentTarget > 0 and startIndex < len(candidates):
                for i in range(startIndex, len(candidates)):
                    if i > startIndex and candidates[i] == candidates[i - 1]:
                        continue
                    path.append(candidates[i])
                    backtrack(i + 1, currentTarget - candidates[i])
                    path.pop()
                    
        backtrack(0, target)
        
        return res
            