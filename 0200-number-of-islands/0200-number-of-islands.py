class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for row in range(m)]
        res = 0
        
        # for i in range(m):
        #     for j in range(n):
        #         if grid[i][j] == "1" and not visited[i][j]:
        #             res += 1
        #             dfs(i, j)
                    
        def dfs(i,j):
            if i < 0 or i >= m or j < 0 or j >= n:
                return
            
            if grid[i][j] == "1" and not visited[i][j]:
                visited[i][j] = True

                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    res += 1
                    dfs(i, j)
            
        return res