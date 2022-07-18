class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [0]
        
        for j in range(1, len(temperatures)):
            if temperatures[j] <= temperatures[stack[-1]]:
                stack.append(j)
            else:
                while stack and temperatures[j] > temperatures[stack[-1]]:
                    idx = stack.pop()
                    res[idx] = j - idx
                stack.append(j)
        
        return res
                