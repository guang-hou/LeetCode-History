class Solution:
    def __init__(self):
        self.path = []
        self.pathSum = 0
        self.res = []
        
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        
        self.dfs(candidates, target, 0)
        
        return self.res
        
    def dfs(self, candidates, target, nodeStartIndex):
        if self.pathSum == target:
            self.res.append(self.path[:])
            return
        
        if self.pathSum > target:
            return
        
        for i in range(nodeStartIndex, len(candidates)):
            if i > nodeStartIndex and candidates[i] == candidates[i - 1]:
                continue
            item = candidates[i]
            self.path.append(item)
            self.pathSum += item
            self.dfs(candidates, target, i + 1)
            self.path.pop()
            self.pathSum -= item
                       