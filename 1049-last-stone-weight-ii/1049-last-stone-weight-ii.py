class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        m, n = len(stones), sum(stones) // 2
        
        dp = [[0] * (n + 1) for _ in range(m)]
        
        # first row, m == 0
        for j in range(stones[0], n + 1):
            dp[0][j] = stones[0]
        
        for i in range(1, m):
            for j in range(n + 1):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - stones[i]] + stones[i])
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return sum(stones) - 2 * dp[m - 1][n]