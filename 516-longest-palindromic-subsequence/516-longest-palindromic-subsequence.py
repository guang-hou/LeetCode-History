class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * (len(s)) for _ in range(len(s))]
        res = 1
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:  # 矩陣的斜綫
                    dp[i][j] = 1
                elif j == i + 1: # 矩陣斜綫平行的右上一條綫
                    if s[i] == s[j]:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = 1
                else: # 右上其他區域，自然會保證不會out of bound
                    if s[i] == s[j]:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1], dp[i + 1][j - 1] + 2)
                    else:
                        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

                res = max(res, dp[i][j])
        
        return res