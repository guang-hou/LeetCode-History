class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[[0, 0] for col in range(3)] for row in range(n)]
        
        for i in range(n):
            for j in range(3):
                if i == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = - prices[0]
                elif j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = float("-inf")
                else:
                    dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
        
        return dp[n - 1][2][0]