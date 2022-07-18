class Solution:
    def trap(self, height: List[int]) -> int:
        right_larger = [i for i in range(len(height))]
        left_larger = [i for i in range(len(height))]
        
        stack = []
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                right_larger[stack.pop()] = i
            
            stack.append(i)
        
        stack = []
        for i in range(len(height) - 2, -1, -1):
            while stack and height[i] >= height[stack[-1]]:
                left_larger[stack.pop()] = i
            
            stack.append(i)
            
        res = 0
        for i in range(1, len(height) - 1):
            l, r = left_larger[i], right_larger[i]
            w = r - l - 1
            h = min(height[l], height[r]) - height[i]
            res += w * h
        
        return res
        
        