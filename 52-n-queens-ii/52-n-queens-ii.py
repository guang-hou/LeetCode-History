class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [["."] * n for _ in range(n)]
        path, res = [], []
        
        
        def backtrack(row):
            if row == n:
                res.append(path[:])
                return
            
            for col in range(n):
                if is_valid(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."
                    
        
        def is_valid(row, col):
            for k in range(n):
                if board[k][col] == "Q" or board[row][k] == "Q":
                    return False
                
                k = 0
                while row - k > -1 and col + k < n:
                    if board[row - k][col + k] == "Q":
                        return False
                    k += 1
                
                k = 0
                while row + k < n and col + k < n:
                    if board[row + k][col + k] == "Q":
                        return False
                    k += 1
                
                k = 0
                while row + k < n and col - k > -1:
                    if board[row + k][col - k] == "Q":
                        return False
                    k += 1
                    
                k = 0
                while row - k > -1 and col - k > -1:
                    if board[row - k][col - k] == "Q":
                        return False
                    k += 1
            return True
                
        
        backtrack(0)
        
        return len(res)
                    
                