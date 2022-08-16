class Solution:
    def __init__(self):
        self.isUsed = []
        self.path = []
        self.res = []
        
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.isUsed = [False] * len(nums)
        self.dfs(nums)
        
        return self.res
    
    def dfs(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return
        
        used = set()
        for i in range(len(nums)):
            num = nums[i]
            if not self.isUsed[i]:
                if num not in used:
                    self.path.append(num)
                    self.isUsed[i] = True
                    used.add(num)
                    self.dfs(nums)
                    self.path.pop()
                    self.isUsed[i] = False
