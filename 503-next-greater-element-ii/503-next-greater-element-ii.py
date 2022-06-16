class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)  # next greater element
        stack = [0]             # index in nums
        
        for i in range(1, len(nums) * 2):
            cur_index = i % len(nums)
            while stack and nums[cur_index] > nums[stack[-1]]:
                res[stack[-1]] = nums[cur_index]
                stack.pop()
            stack.append(cur_index)
        
        return res
        
        