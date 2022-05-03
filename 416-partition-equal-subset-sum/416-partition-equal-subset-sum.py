class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1: return False
        
        m = len(nums)
        n = total // 2
        
        dp = [[0] * (n + 1) for _ in range(m)]
        
        for j in range(n + 1):
            if dp[0][j] >= nums[0]:
                dp[0][j] = nums[0]
        
        
        for i in range(1, m):
            for j in range(n + 1):
                if j >= nums[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]] + nums[i]) 
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m - 1][n] == n
    
    