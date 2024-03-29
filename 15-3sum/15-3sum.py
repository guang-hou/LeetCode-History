class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3: return None
        
        nums.sort()
        res = []
        
        for i in range(len(nums)-2):
            if nums[i] > 0: break
                
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1
            
            while left < right:
                a, b, c = nums[i], nums[left], nums[right]
                tmp_sum = a + b+ c
                
                if tmp_sum == 0:
                    res.append([a, b, c])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif tmp_sum < 0:
                    left += 1
                else:
                    right -= 1
                
        return res