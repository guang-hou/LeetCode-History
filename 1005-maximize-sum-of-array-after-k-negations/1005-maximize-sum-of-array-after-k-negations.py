class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] >= 0 and k % 2 ==0: return sum(nums)
        
        n = len(nums)

        for i in range(n):
            if k > 0 and nums[i] < 0:
                nums[i]= - nums[i]
                k -= 1
            
        if k > 0 and k % 2 == 1:
            res = sum(nums) - 2 * min(nums)
        else:
            res = sum(nums)
            
        return res