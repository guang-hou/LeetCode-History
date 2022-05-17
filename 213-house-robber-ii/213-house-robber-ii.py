class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return nums[0]
        elif len(nums) == 1:
            return max(nums)
        
        dp1 = [[0, 0] for _ in range(len(nums))] # rob house 0
        
        dp1[0] = [nums[0], nums[0]]
        dp1[1] = [nums[0], nums[0]]
        
        for i in range(2, len(nums) - 1):
            dp1[i][0] = max(dp1[i - 1])
            dp1[i][1] = dp1[i - 1][0] + nums[i]
        
        dp2 = [[0, 0] for _ in range(len(nums))] # not rob house 0
        
        dp2[0] = [0, 0]
        dp2[1] = [0, nums[1]]
        
        for i in range(2, len(nums)):
            dp2[i][0] = max(dp2[i - 1])
            dp2[i][1] = dp2[i - 1][0] + nums[i]
        
        return max(max(dp1[-2]), max(dp2[-1]))