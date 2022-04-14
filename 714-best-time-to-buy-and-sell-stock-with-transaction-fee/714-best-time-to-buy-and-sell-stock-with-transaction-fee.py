class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
    
        length = len(prices)
        dp = [[0] * 2 for _ in range(length)]  # [天数][是否持有股票]
        dp[0][0] = 0                    # dp[i][0] 表示第i天不持有股票所得现金
        dp[0][1] = -prices[0]           # dp[i][1] 表示第i天持有股票所得最多现金
        for i in range(1, length):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i] - fee) 
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return max(dp[-1][0], dp[-1][1])