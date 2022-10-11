class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[[0, 0] for _ in range(k + 1)] for _ in range(n)]
        
        for i in range(n):
            dp[i][0][0] = 0
            dp[i][0][1] = float("-inf")
        
        for j in range(1, k + 1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        
        for i in range(1, n):
            for j in range(1, k + 1):  
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                
        return dp[-1][k][0]