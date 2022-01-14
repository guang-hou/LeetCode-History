class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4: return None
        
        nums.sort()
        N = len(nums)
        res = []
        
        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            first_target = target - nums[i]
            for j in range(i + 1, N):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                second_target = first_target - nums[j]
                
                left, right = j + 1, N - 1
                
                while left < right:
                    local_sum = nums[left] + nums[right]
                    
                    if local_sum < second_target:
                        left += 1
                    elif local_sum > second_target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left + 1] == nums[left]:
                            left += 1
                        while left < right and nums[right - 1] == nums[right]:
                            right -= 1
                        
                        left += 1
                        right -= 1
        return res