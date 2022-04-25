class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for _ in range(m)]
        
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            dp[0][0] = 1
        
        for i in range(1, n):
            if obstacleGrid[0][i]:
                dp[0][i] = 0
                break
            else:
                dp[0][i] = 1
        
        for j in range(1, m):
            if obstacleGrid[j][0]:
                dp[j][0] = 0
                break
            else:
                dp[j][0] = 1
        
        for j in range(1, m):
            for i in range(1, n):
                if obstacleGrid[j][i]:
                    dp[j][i] = 0
                else:
                    dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        
        # print(dp)
        
        return dp[m - 1][n - 1]