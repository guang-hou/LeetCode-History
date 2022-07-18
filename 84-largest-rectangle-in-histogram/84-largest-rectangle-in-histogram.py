class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left_smaller = [-1] * n  # store the index of left first smaller element
        right_smaller = [n] * n  # store the index of right first smaller element
        
        # calculate right_smaller
        stack = []
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                right_smaller[stack.pop()] = i
            stack.append(i)
          
        # calculate left_smaller
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] < heights[stack[-1]]:
                left_smaller[stack.pop()] = i
            stack.append(i)
            

        res = 0
        for i in range(n):
            area = heights[i] * (right_smaller[i] - left_smaller[i] - 1)
            res = max(res, area)
        
        return res