class Solution:
    def __init__(self):
        self.board = []
        self.res = []
        
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.board = [['.'] * n for _ in range(n)]
        
        #print(self.board)
        
        self.dfs(0, n)
        
        return self.res
        
        
    def dfs(self, row, n):
        if row == n:
            self.res.append(["".join(row) for row in self.board])
            return
        
        for col in range(n):
            if self.isValid(row, col, n):
                self.board[row][col] = 'Q'
                self.dfs(row + 1, n)
                self.board[row][col] = '.'
        
    
    def isValid(self, row, col, n):
        for i in range(n):
            if i < row and self.board[i][col] == 'Q':
                return False
            
        for j in range(n):
            if j < col and self.board[row][j] == 'Q':
                return False
        
        i, j = row, col
        while i < n and j > -1:
            if self.board[i][j] == 'Q':
                return False
            i += 1
            j -= 1
        
        i, j = row, col
        while i > -1 and j < n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
            
        i, j = row, col
        while i < n and j < n:
            if self.board[i][j] == 'Q':
                return False
            i += 1
            j += 1
        
        i, j = row, col
        while i > -1 and j > -1:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        return True
        
        
        