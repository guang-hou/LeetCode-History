class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        t = list(s)
        N = len(s)
        
        if N == 1: return s
        
        for i in range(0, N, 2*k):
            left = i
            right = min(i + k - 1, N - 1)

            while left < right:
                t[left], t[right] = t[right], t[left]
                left += 1
                right -= 1
        
        return "".join(t)
            
            
            
            
            
                       
        