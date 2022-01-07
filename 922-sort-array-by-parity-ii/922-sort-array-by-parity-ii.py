class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        slow, fast = 0, 0
        
        for fast in range(len(nums)):
            if fast % 2 == 1 and nums[fast] % 2 == 0:
                while nums[slow] % 2 == 0:
                    slow += 2
                nums[slow], nums[fast] = nums[fast], nums[slow]
        
        return nums
        