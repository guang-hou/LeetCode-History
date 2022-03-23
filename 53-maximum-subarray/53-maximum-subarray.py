class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <= 1: return sum(nums)
        
        s, res = -float('inf'), -float('inf')
        
        for i in range(len(nums)):
            if s < 0:
                s = nums[i]
            else:
                s += nums[i]
                
            res = max(res, s)
        
        return res