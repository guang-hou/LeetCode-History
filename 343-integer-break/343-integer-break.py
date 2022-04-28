class Solution:
    def integerBreak(self, n: int) -> int:

        dp = [1] * (1 + n)
        
        for i in range(3, n + 1):
            for k in range(1, i // 2 + 1):
                dp[i] = max(dp[i], k * (i - k), k * dp[i - k], dp[k] * (i - k), dp[k] * dp[i - k]) 
        
        return dp[n]
        