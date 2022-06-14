class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        res = 0
        
        for i in range(len(s) - 1, -1, -1):
            for j in range(len(s)):
                if s[i] == s[j]:
                    if i == j or (i + 1) == j:
                        dp[i][j] = 1
                    elif j >  i + 1 and dp[i + 1][j - 1]:
                        dp[i][j] = 1
                
                res += dp[i][j]
        
        return res
                        
        