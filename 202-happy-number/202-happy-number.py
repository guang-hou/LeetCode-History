class Solution:
    def isHappy(self, n: int) -> bool:
        pre = set()
        
        while True:
            pre.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
            else:
                if n in pre:
                    return False
        
    def sumOfSquares(self, n):
        res = 0
        
        while n > 0:
            res += (n % 10) ** 2
            n = n // 10
        
        return res
        