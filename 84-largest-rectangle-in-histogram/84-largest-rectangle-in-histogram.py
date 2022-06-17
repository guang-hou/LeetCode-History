class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        right_smaller = [size - 1] * size
        left_smaller = [0] * len(heights)
        
        stack = [0]
        
        for i in range(1, size):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                right_smaller[index] = i
            
            stack.append(i)
        
        while stack:
            index = stack.pop()
            right_smaller[index] = size
        
        stack = [size - 1]
        
        for i in range(size - 2, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                index = stack.pop()
                left_smaller[index] = i
            
            stack.append(i)
        
        while stack:
            index = stack.pop()
            left_smaller[index] = -1
        
        res = 0
        for i in range(size):
            cur = heights[i] * (right_smaller[i] - left_smaller[i] - 1)
            res = max(res, cur)
        
        return res
            
        