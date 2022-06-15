class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp = [[0] * len(s) for _ in range(len(s))]
        start, end = 0, 0
        
        for i in range(len(s)):
            dp[i][i] = 1
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):     
                if s[i] != s[j]:
                    dp[i][j] = 0
                else:
                    if j == i + 1 or dp[i + 1][j - 1]:
                        dp[i][j] = 1
                        if j - i > end - start:
                            start, end = i, j
        
        return s[start: end + 1]