class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        index = 1
        res = [[0] * n for _ in range(n)]
        
        while top < bottom and left < right:
            for i in range(left, right):
                res[top][i] = index
                index += 1
            
            for i in range(top, bottom):
                res[i][right] = index
                index += 1
            
            for i in range(right, left, -1):
                res[bottom][i] = index
                index += 1
            
            for i in range(bottom, top, -1):
                res[i][left] = index
                index += 1
            
            top += 1
            bottom -= 1
            left += 1
            right -= 1
        
        if top == bottom and left == right:
            res[top][left] = n * n
        
        return res
            