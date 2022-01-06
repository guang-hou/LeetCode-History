class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = 0, sum(nums[1:])
        
        for i in range(len(nums) - 1):
            if left == right:
                return i
            else:
                left += nums[i]
                right -= nums[i + 1]
        
        if left == 0:
            return len(nums) - 1
        
        return -1
            