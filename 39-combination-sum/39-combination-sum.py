class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        #candidates.sort()
        
        def backtrack(i):
            if sum(path) == target:
                res.append(path[:])
                return
            elif sum(path) < target:
                for j in range(i, len(candidates)):
                    #if j > i and candidates[j] == candidates[j - 1]:
                    #    continue
                    path.append(candidates[j])
                    backtrack(j)
                    path.pop()
            else:
                return
        
        backtrack(0)
        return res