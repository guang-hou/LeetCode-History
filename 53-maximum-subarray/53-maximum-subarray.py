class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        
        dp = [0] * n
        
        dp[0] = nums[0]
        
        for i in range(1, n):
            if nums[i] >= dp[i - 1] + nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = nums[i] + dp[i - 1]
        
        return max(dp)