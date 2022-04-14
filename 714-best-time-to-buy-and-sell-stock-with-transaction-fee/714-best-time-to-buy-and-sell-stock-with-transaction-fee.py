class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [[0] * 2 for i in range(len(prices))] # 0: no stock, 1: stock
        
        dp[0] = [0, -prices[0]]
        
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            dp[i][1] = max(dp[i - 1][0] - prices[i], dp[i - 1][1])
        
        print(dp)
        return max(dp[-1])