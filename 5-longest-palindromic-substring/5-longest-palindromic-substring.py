class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        res = [1, 0, 0]  # length, i, j
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):     
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    if j == i + 1 or dp[i + 1][j - 1]:
                        dp[i][j] = 1
                        if j - i + 1 > res[0]:
                            res = [j - i + 1, i, j]
        
        return s[res[1]: res[2] + 1]