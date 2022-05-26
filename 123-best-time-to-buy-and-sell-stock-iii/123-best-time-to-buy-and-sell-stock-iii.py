class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0] * 5 for _ in range(len(prices))] # 1_no, 1_yes, 2_no, 2_yes, 2_yes_no
        
        dp[0] = [0, -prices[0], float('-inf'), float('-inf'), float('-inf')]
        
        for i in range(1, len(prices)):
            dp[i][0] = dp[i - 1][0]
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
            dp[i][2] = max(dp[i - 1][2], dp[i - 1][1] + prices[i])
            dp[i][3] = max(dp[i - 1][3], dp[i - 1][2] - prices[i])
            dp[i][4] = max(dp[i - 1][4], dp[i - 1][3] + prices[i])
            
        return max(dp[-1])