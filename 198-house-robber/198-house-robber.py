class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [[0, 0] for _ in range(len(nums))] # 0 no robbery, 1 robbery
        dp[0] = [0, nums[0]]
        
        for i in range(1, len(nums)):
            dp[i][0] = max(dp[i - 1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        
        return max(dp[-1])