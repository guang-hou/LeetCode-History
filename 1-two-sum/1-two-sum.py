class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in diff:
                return [i, diff[num]]
            else:
                diff[target - num] = i
        
        return None