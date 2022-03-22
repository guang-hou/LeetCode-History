class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)
        
        # if len(nums) == 2:
        #     if nums[0] != nums[1]: 
        #         return 2
        #     else:
        #         return 1

        res = 0
        i = 1
        while i < len(nums):
            if nums[i] > nums[i - 1]:
                res += 1
                while i + 1 < len(nums) and nums[i + 1] >= nums[i]:
                    i += 1
            elif nums[i] < nums[i - 1]:
                res += 1
                while i + 1 < len(nums) and nums[i + 1] <= nums[i]:
                    i += 1
            i += 1
        
        return res + 1

        
        