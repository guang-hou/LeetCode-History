class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[[0, 0] for col in range(k + 1)] for row in range(n)]

        for i in range(n):
            for j in range(k + 1):  
                if j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = float("-inf")
                elif i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[0]
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                
        return dp[-1][k][0]