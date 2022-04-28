class Solution:
    def integerBreak(self, n: int) -> int:
        # n = 10
        dp = [1] * (1 + n)
        
        for i in range(2, n + 1):
            for k in range(1, i // 2 + 1):
                dp[i] = max(dp[i], k * (i - k), k * dp[i - k], dp[k] * (i - k), dp[k] * dp[i - k])
                # print(i, k, dp[i], k * (i - k), k * dp[i - k], dp[k] * (i - k), dp[k] * dp[i - k])
        
        return dp[n]
        