class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0
        
        stack = [0]
        res = 0
        
        for i in range(1, len(height)):
            while stack and height[i] > height[stack[-1]]:
                middle = stack.pop()
                if stack:
                    left = stack[-1]
                    res += (min(height[i], height[left]) - height[middle]) * (i - left - 1)
            #if stack and height[i] == height[stack[-1]]:  ## 隐含实现了
            #    stack.pop()
        
            stack.append(i)
            
        return res
                    
                
                
                
        