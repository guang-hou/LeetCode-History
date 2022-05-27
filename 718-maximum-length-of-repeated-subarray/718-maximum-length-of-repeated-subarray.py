class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        length1, length2 = len(nums1), len(nums2)
        res = 0
        
        dp = [[0] * length2 for _ in range(length1)]
        
        # first row
        for j in range(0, length2):
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
                res = max(res, dp[0][j])
        
        # first column
        for i in range(0, length1):
            if nums2[0] == nums1[i]:
                dp[i][0] = 1
                res = max(res, dp[i][0])
        
        for i in range(1, length1):
            for j in range(1, length2):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                #dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
                res = max(res, dp[i][j])
        
        return res