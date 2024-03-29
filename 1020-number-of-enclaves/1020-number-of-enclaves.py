class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        
        for i in range(m):
            self.dfs(i, 0, grid, visited)
            self.dfs(i, n - 1, grid, visited)
            
        for j in range(n):
            self.dfs(0, j, grid, visited)
            self.dfs(m - 1, j, grid, visited)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    res += 1
        
        return res
        
    def dfs(self, i, j, grid, visited):
        m, n = len(grid), len(grid[0])
        
        if i < 0 or i == m or j < 0 or j == n:
            return 0
        
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True

            self.dfs(i - 1, j, grid, visited)
            self.dfs(i + 1, j, grid, visited)
            self.dfs(i, j - 1, grid, visited)
            self.dfs(i, j + 1, grid, visited)
            
