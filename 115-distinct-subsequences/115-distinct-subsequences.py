class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(t) > len(s):
            return 0
        
        dp = [[0] * len(s) for _ in range(len(t))]  # dp[i][j]  for t[i]   s[j]
        
        for j in range(0, len(s)): # dp[0][j]  t[0]   s[j]
            if s[j] == t[0]:
                if j == 0:
                    dp[0][0] = 1
                else:
                    dp[0][j] = dp[0][j - 1] + 1
            else:
                if j == 0:
                    dp[0][0] = 0
                else:
                    dp[0][j] = dp[0][j - 1]          
            
            
        for i in range(1, len(t)):
            for j in range(1, len(s)):
                if t[i] == s[j]:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]
                    
        #print(dp)
        
        return dp[-1][-1]