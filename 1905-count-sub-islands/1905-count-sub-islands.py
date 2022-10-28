class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and grid1[i][j] == 0 and not visited[i][j]:
                    self.dfs(i, j, grid1, grid2, visited)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    res += 1
                    self.dfs(i, j, grid1, grid2, visited)
        
        return res
        
    def dfs(self, i, j, grid1, grid2, visited):
        m, n = len(grid2), len(grid2[0])
        
        if i < 0 or i == m or j < 0 or j == n:
            return 
        
        if grid2[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            
            self.dfs(i - 1, j, grid1, grid2, visited)
            self.dfs(i + 1, j, grid1, grid2, visited)
            self.dfs(i, j - 1, grid1, grid2, visited)
            self.dfs(i, j + 1, grid1, grid2, visited)
