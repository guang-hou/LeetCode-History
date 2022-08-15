class Solution:
        
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        prev = self.permute(nums[:-1])
        
        return [p[:i] + [nums[-1]] + p[i:] for p in prev for i in range(len(nums))] 