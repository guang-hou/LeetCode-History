class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        size = len(temperatures)
        res = [0] * size
        stack = [0]
        
        for i in range(1, size):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i - index

            stack.append(i)
                
        
        return res