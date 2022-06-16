class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        
        dp = [1] * len(nums)       # length of the longest increasing subsequence
        count = [1] * len(nums)    # count of number of subsequence with max length
        max_length = 1
        
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        count[i] = count[j]
                        dp[i] = dp[j] + 1

                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]
            
            max_length = max(max_length, dp[i])
            
        res = 0
        for i in range(len(nums)):
            if dp[i] == max_length:
                res += count[i]
        
        return res
            