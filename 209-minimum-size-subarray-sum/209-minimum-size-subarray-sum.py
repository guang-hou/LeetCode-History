class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, right = 0, 0
        total = nums[0]
        res = float("inf")
        
        while (left <= right and right < len(nums)):
            if total < target:
                right += 1
                if right < len(nums):
                    total += nums[right]
            else:
                while total >= target:
                    res = min(res, right - left + 1)
                    if res == 1:
                        return res
                    total -= nums[left]
                    left += 1
        
        if res <= len(nums):
            return res
        else:
            return 0