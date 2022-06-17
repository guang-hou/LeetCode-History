class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0
        
        stack = [0]
        for i in range(1, size):
            while stack and heights[i] < heights[stack[-1]]:
                middle = stack.pop()
                if stack:
                    left = stack[-1]
                else:
                    left = -1
                area = heights[middle] * (i - left - 1)
                res = max(res, area)
            
            stack.append(i)
        
        while stack:
            right = size
            middle = stack.pop()
            if stack:
                left = stack[-1]
            else:
                left = -1
            area = heights[middle] * (right - left - 1)
            res = max(res, area)
        
        return res
            
        