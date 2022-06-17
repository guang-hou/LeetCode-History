class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.insert(0, 0)
        heights.append(0)  # 这样left_index 一直在，stack不会变为空
        stack = [0]
        result = 0
        for i in range(1, len(heights)):
            while heights[i] < heights[stack[-1]]:
                mid_height = heights[stack[-1]]
                stack.pop()
                # area = width * height
                area = (i - stack[-1] - 1) * mid_height
                result = max(area, result)
            stack.append(i)
        return result