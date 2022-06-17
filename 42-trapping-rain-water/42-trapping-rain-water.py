class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        max_left = [height[0]] * len(height)    # i left side's max height
        max_right = [height[-1]] * len(height)  # i right sides' max height
        
        for i in range(1, len(height)):
            max_left[i] = max(height[i], max_left[i - 1])
        
        for j in range(len(height) - 2, -1, -1):
            max_right[j] = max(height[j], max_right[j + 1])
        
        res = 0
        for k in range(1, len(height) - 1):
            res += min(max_left[k], max_right[k]) - height[k]
        
        return res
        