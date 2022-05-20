class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = [0] * (len(prices) + 1)
        res = 0
        
        for i in range(1, len(prices)):
            profit[i] = max(prices[i] - prices[i - 1] + profit[i - 1], 0)
            res = max(profit[i], res)
        
        return res