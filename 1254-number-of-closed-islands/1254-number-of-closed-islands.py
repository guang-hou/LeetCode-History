class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for row in range(m)]
        res = 0
        
        for i in range(m):
            self.dfs(grid, i, 0, visited)
            self.dfs(grid, i, n - 1, visited)   
            
        for j in range(n):
            self.dfs(grid, 0, j, visited)
            self.dfs(grid, m - 1, j, visited)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    res += 1
                    self.dfs(grid, i, j, visited)
        
        return res
    
        
    def dfs(self, grid, i, j, visited):
        m, n = len(grid), len(grid[0])
        if (i < 0 or i >= m or j < 0 or j >= n):
            return 0
        
        if grid[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            
            self.dfs(grid, i - 1, j, visited)
            self.dfs(grid, i + 1, j, visited)
            self.dfs(grid, i, j - 1, visited)
            self.dfs(grid, i, j + 1, visited)