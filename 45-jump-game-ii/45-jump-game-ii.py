class Solution:
    def jump(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1: return 0
        
#         step = 1
#         i = 0
#         cover = nums[0]
#         next_cover = 0
        
#         if cover >= n - 1: return 1
        
#         while i <= cover:
#             cur_next_cover = nums[i] + i
#             next_cover = max(next_cover, cur_next_cover)
#             # if next_cover >= n - 1:
#             #     return step + 1

#             if i == cover:
#                 cover = next_cover
#                 step += 1
            
#             if cover >= n - 1:
#                 return step
        
#             i += 1
            

        n = len(nums)
        if n == 1: return 0
        if nums[0] >= n - 1: return 1
        
        cover = nums[0]
        next_cover = nums[0]
        step = 1
        
        for i in range(1, n):
            if i <= cover:
                next_cover = max(next_cover, nums[i] + i)
                if next_cover >= n - 1:
                    return step + 1
            if i == cover:
                cover = next_cover
                step += 1
        
        return step
        
                
            
            