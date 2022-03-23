class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        
        s, res = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if s < 0:
                s = nums[i]
            else:
                s += nums[i]
                
            res = max(res, s)
        
        return res