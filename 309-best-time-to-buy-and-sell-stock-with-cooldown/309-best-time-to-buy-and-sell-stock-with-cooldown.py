class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if (len(prices)) == 1:
            return 0
            
        dp = [[float('-inf')] * 3 for _ in range(len(prices))]
        
        dp[0][0] = -prices[0]
        
        for i in range(1, len(prices)):
            dp[i][0] =  max(dp[i - 1][0], dp[i - 1][2] - prices[i], -prices[i])
            dp[i][1] =  max(dp[i - 1][1], dp[i - 1][0] + prices[i])
            dp[i][2] =  max(dp[i - 1][2], dp[i - 1][1])
        
        return max(0, max(dp[-1]))