class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if target > sum_nums or target < -sum_nums:  # 背包的大小应该可以容纳[-sum(nums),sum(nums)]这个区间的所有数
            return 0
                    
        len_nums = len(nums)
        
        row, col = len(nums) + 1, 2*sum_nums + 1   # 有len(nums)个元素, 这里用了len(nums) + 1 行
        
        dp = [[0] * (col) for _ in range(row)]  
        
        dp[0][sum_nums] = 1
        
        for i in range(1, row):
            for j in range(col):
                if j + nums[i - 1] < col:
                    dp[i][j] += dp[i - 1][j + nums[i - 1]]
                if j - nums[i - 1] >= 0:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]
        
        return dp[row - 1][sum_nums + target]
        