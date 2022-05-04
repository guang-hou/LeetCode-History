class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        sum_nums = sum(nums)
        if target > sum_nums or target < -sum_nums or (target + sum_nums) % 2 == 1:  
            return 0
                    
        volume = (target + sum_nums) // 2
        
        dp = [0] * (volume + 1) 
        
        dp[0] = 1
        
        for num in nums:
            for i in range(volume, num - 1, -1):
                dp[i] += dp[i - num]
        
        return dp[volume]
        