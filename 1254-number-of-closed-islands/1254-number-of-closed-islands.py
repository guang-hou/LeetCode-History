class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for row in range(m)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    if(self.dfs(grid, i, j, visited, m, n) == 0):
                        res += 1
        
        return res
        
    def dfs(self, grid, i, j, visited, m, n):
        if (i < 0 or i >= m or j < 0 or j >= n):
            return 0
        
        if grid[i][j] == 0 and not visited[i][j]:
            visited[i][j] = True
            
            l = self.dfs(grid, i - 1, j, visited, m, n)
            r = self.dfs(grid, i + 1, j, visited, m, n)
            u = self.dfs(grid, i, j - 1, visited, m, n)
            d = self.dfs(grid, i, j + 1, visited, m, n)
            
            if (i == 0 or i == m - 1 or j == 0 or j == n - 1):
                return -1
            
            if (l + r + u + d) != 0:
                return -1
            
        return 0