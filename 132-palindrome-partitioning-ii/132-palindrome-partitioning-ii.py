class Solution:
    def minCut(self, s: str) -> int:
        isPar = [[False] * len(s) for _ in range(len(s))]
        
        dp = [len(s)] * len(s)
        dp[0] = 0

        for i in range(len(s)):
            isPar[i][i] = True
            if i < len(s) - 1 and s[i] == s[i + 1]:
                isPar[i][i + 1] = True
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 2, len(s)):
                if s[i] == s[j] and isPar[i + 1][j - 1]:
                    isPar[i][j] = True

        
        for i in range(1, len(s)):
            if isPar[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if isPar[j + 1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
                
        
        return dp[len(s) - 1]