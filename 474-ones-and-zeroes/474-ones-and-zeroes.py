class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        len_strs = len(strs)
        zero_count = [0] * len_strs
        one_count = [0] * len_strs
        
        for i, str in enumerate(strs):
            for char in str:
                if char == "0":
                    zero_count[i] += 1
                elif char == "1":
                    one_count[i] += 1
        
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(len_strs)]  # dp[i][j][k]  the size of the largest subset of strs[0-i] for at most j 0's and k 1's
        
        # initialization dp[0]
        for j in range(zero_count[0], m + 1):
            for k in range(one_count[0], n + 1):
                dp[0][j][k] = 1
                
        for i in range(1, len_strs):
            for j in range(m + 1):
                for k in range(n + 1):
                    if j >= zero_count[i] and k >= one_count[i]:
                        dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zero_count[i]][k - one_count[i]] + 1)
                    # elif j == zero_count[i] and k == one_count[i]:
                    #     dp[i][j][k] = max(dp[i - 1][j][k], dp[i - 1][j - zero_count[i]][k - one_count[i]] + 1)
                    else:
                        dp[i][j][k] = dp[i - 1][j][k]
        
        return dp[len_strs - 1][m][n]
            
        