class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        
        for i in range(len(nums)):
            if i <= reach:
                cur_reach = nums[i] + i
                reach = max(reach, cur_reach)
                if reach >= len(nums) - 1:
                    return True
        
        return False