class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s)) for _ in range(len(s))]
        res = 1
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s)):
                if j >= i:
                    if i == j:
                        dp[i][j] = 1
                    elif j == i + 1:
                        if s[i] == s[j]:
                            dp[i][j] = 2
                        else:
                            dp[i][j] = 1
                    elif i < len(s) - 1 and j > i + 1 and j > 0:
                        if s[i] == s[j]:
                            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1] + 2)
                        else:
                            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
                            
                    res = max(res, dp[i][j])
        
        return res