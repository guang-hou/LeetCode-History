class Solution:
    def isHappy(self, n: int) -> bool:
        record= set()
        
        while True:
            n = self.sumOfSquares(n)
            if n == 1:
                return True
            elif n in record:
                return False
            else:
                record.add(n)
        
    def sumOfSquares(self, n):
        res = 0
        
        while n > 0:
            res += (n % 10) ** 2
            n = n // 10
        
        return res
        