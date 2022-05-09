class Solution:
    def balancedStringSplit(self, s: str) -> int:
        num_R, num_L = 0, 0
        res = 0
        
        for c in s:
            if c == "R":
                num_R += 1
            else:
                num_L += 1
            
            if num_R == num_L:
                res += 1
                num_R, num_L = 0, 0
        
        return res