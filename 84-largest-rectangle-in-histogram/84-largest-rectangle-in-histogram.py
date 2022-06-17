class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # 加入一个小的值，那么原来队列中的值都会被弹出得到计算
        m = len(heights)
        stack = [0]
        res = 0
        
        for i in range(1, m):
            while stack and heights[i] < heights[stack[-1]]:
                idx = stack.pop()  # 计算高度列的index
                right_idx = i
                
                if stack: 
                    left_idx = stack[-1] # handle the case where thiere is no smaller element
                else: 
                    left_idx = -1
                area = (right_idx - left_idx - 1) * heights[idx]
                res = max(res, area)
            stack.append(i)

        return res