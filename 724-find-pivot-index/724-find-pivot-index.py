class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums[1:])
        
        for i in range(len(nums)):
            if left == right:
                return i
            elif i < len(nums) - 1:
                left += nums[i]
                right -= nums[i + 1]
        
        return -1
            