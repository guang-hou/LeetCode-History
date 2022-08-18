class Solution:       
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.dfs(0, 0, board)
    
    
    def dfs(self, row, col, board):
        if row == len(board):
            return True
    
        if board[row][col] == '.':
            for num in range(1, 10):
                if self.isValid(board, row, col, num):
                    board[row][col] = str(num)
                    if col == len(board) - 1:
                        if self.dfs(row + 1, 0, board):
                            return True
                    else:
                        if self.dfs(row, col + 1, board):
                            return True
                    board[row][col] = '.'
        else:
            if col == len(board) - 1:
                if self.dfs(row + 1, 0, board):
                    return True
            else:
                if self.dfs(row, col + 1, board):
                    return True
        
        return False
        
    def isValid(self, board, row, col, num):
        n = len(board)
        
        # check the row
        for j in range(n):
            if board[row][j] == str(num):
                return False
        
        # check the col
        for i in range(n):
            if board[i][col] == str(num):
                return False
        
        # check the small grid
        gridUppLeftX, gridUppLeftY = (row // 3) * 3, (col // 3) * 3
        
        for i in range(3):
            for j in range(3):
                if board[gridUppLeftX + i][gridUppLeftY + j] == str(num):
                    return False
                
        return True
        
        
        