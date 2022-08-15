class Solution:
    def __init__(self):
        self.used = set()
        self.path = []
        self.res = []
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.dfs(nums)
        
        return self.res
        
    def dfs(self, nums):
        if len(self.path) == len(nums):
            self.res.append(self.path[:])
            return
        
        for num in nums:
            if num not in self.used:
                self.used.add(num)
                self.path.append(num)
                self.dfs(nums)
                self.used.remove(num)
                self.path.pop()