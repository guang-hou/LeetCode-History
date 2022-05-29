class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)
        
        
        dp = [[float('inf')] * len(word1) for _ in range(len(word2))]
        
        # initialize
        for i in range(0, len(word2)): # j == 0
            if word2[i] == word1[0]:
                dp[i][0] = i
            elif i > 0:
                dp[i][0] = min(i + 2, dp[i - 1][0] + 1)
            else:
                dp[i][0] = 1
        
        for j in range(1, len(word1)): # i == 0
            if word1[j] == word2[0]:
                dp[0][j] = j
            else:
                dp[0][j] = dp[0][j - 1] + 1
        
        for i in range(1, len(word2)):
            for j in range(1, len(word1)):
                if word2[i] == word1[j]:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i][j - 1] + 1, dp[i - 1][j] + 1)
                else:
                    dp[i][j] = min(dp[i - 1][j - 1] + 1, dp[i][j - 1] + 1, dp[i - 1][j] + 1)
        
        print(dp)
        
        return dp[-1][-1]