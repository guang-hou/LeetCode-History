class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 2 for _ in range(len(prices))]
        
        dp[0] = [0, -prices[0]]
        res = 0
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(- prices[i], dp[i - 1][1])
            res = max(dp[i])
        
        print(dp)
        return res