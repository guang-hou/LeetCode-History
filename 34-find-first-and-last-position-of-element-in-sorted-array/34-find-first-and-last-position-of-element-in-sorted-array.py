class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums: 
            return [-1,-1]
        
        left, right = 0, len(nums) - 1
        
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                left, right = middle, middle
                while left >=0 and nums[left] == target:
                    left -= 1
                while right < len(nums) and nums[right] == target:
                    right += 1
                return [left + 1, right - 1]
        
        return [-1, -1]
                    
                    