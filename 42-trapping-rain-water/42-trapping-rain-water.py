class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        right_max = [0] * len(height)
        left_max = [0] * len(height)
        
        largest = height[0]
        for i in range(1, len(height) - 1):
            if height[i] > largest:
                left_max[i] = height[i]
                largest = height[i]
            else:
                left_max[i] = largest
        
                
        largest = height[len(height) - 1]
        for i in range(len(height) - 2, 0, -1):
            if height[i] > largest:
                right_max[i] = height[i]
                largest = height[i]
            else:
                right_max[i] = largest
        
        res = 0
        for i in range(1, len(height) - 1):
            res +=  min(left_max[i], right_max[i]) - height[i]
        
        return res