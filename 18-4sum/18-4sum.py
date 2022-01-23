class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return None
        
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                local_target = target - nums[i] - nums[j]
                
                left, right = j + 1, len(nums) - 1
                
                while left < right:
                    a, b = nums[left], nums[right]
                    if a + b < local_target:
                        left += 1
                    elif a + b > local_target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], a, b])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        left += 1
                        right -= 1
            
        return res