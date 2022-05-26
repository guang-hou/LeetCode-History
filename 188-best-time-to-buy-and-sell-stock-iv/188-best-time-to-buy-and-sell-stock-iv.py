class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        length = len(prices)
        
        if length == 0 or k == 0:
            return 0
        
        dp = [[float('-inf')] * (2 * k + 1) for _ in range(length)]
        dp[0][0], dp[0][1] = 0, -prices[0]
        
        for i in range(1, length):
            for j in range(0, 2 * k + 1):
                if j == 0:
                    dp[i][j] = dp[i - 1][j]
                elif j == 2 * k:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
                elif j % 2 == 1:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - prices[i])
                elif j % 2 == 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + prices[i])
        
        return max(dp[-1])