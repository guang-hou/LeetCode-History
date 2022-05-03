class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        m, n = len(stones), sum(stones) // 2
        
        dp = [0] * (n + 1)
        
        for i in range(m):
            for j in range(n, stones[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - stones[i]] + stones[i])
        
        return sum(stones) - 2 * dp[n]