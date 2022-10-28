class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid2), len(grid2[0])
        visited = [[False] * n for _ in range(m)]
        res = 0
        
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1 and not visited[i][j]:
                    if (self.dfs(i, j, grid1, grid2, visited)):
                        res += 1
        
        return res
        
    def dfs(self, i, j, grid1, grid2, visited):
        m, n = len(grid2), len(grid2[0])
        
        if i < 0 or i == m or j < 0 or j == n:
            return True
        
        if grid2[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            
            l = self.dfs(i - 1, j, grid1, grid2, visited)
            r = self.dfs(i + 1, j, grid1, grid2, visited)
            u = self.dfs(i, j - 1, grid1, grid2, visited)
            d = self.dfs(i, j + 1, grid1, grid2, visited)
            
            if grid1[i][j] != 1:
                return False
            
            return l and r and u and d
        
        return True