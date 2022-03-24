class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] >= 0 and k % 2 ==0: return sum(nums)
        
        n = len(nums)
        res = 0

        m = 0
        for i in range(n):
            if i < k and nums[i] < 0:
                nums[i]= - nums[i]
                m += 1

        if m == 0:
            res = sum(nums) - 2 * nums[0]
            
        if m < k and (k - m) % 2 == 1:
            if m == n:
                negative = nums[-1]
            else:
                negative = min(nums[m], nums[m - 1])
            res = sum(nums) - 2 * negative
        else:
            res = sum(nums)
            
        return res