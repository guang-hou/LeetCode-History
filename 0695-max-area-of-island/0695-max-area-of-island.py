class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    res = max(res, self.dfs(i, j, grid, visited))
        return res
    
        
    def dfs(self, i, j, grid, visited):
        m, n = len(grid), len(grid[0])
        res = 0
        
        if i < 0 or i == m or j < 0 or j == n:
            return 0
        
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            res = 1
            
            res += self.dfs(i - 1, j, grid, visited)
            res += self.dfs(i + 1, j, grid, visited)
            res += self.dfs(i, j - 1, grid, visited)
            res += self.dfs(i, j + 1, grid, visited)
            
        return res