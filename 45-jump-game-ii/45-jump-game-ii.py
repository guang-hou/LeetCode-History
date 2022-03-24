class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        
        step = 1
        i = 0
        cover = nums[0]
        next_cover = 0
        
        if cover >= n - 1: return 1
        
        while i <= cover:
            cur_next_cover = nums[i] + i
            next_cover = max(next_cover, cur_next_cover)
            # if next_cover >= n - 1:
            #     return step + 1
            

            if i == cover:
                cover = next_cover
                step += 1
            
            if cover >= n - 1:
                return step
        
            i += 1
                
            
            