class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        records = set()
        
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not visited[i][j]:
                    label = self.dfs(grid, visited, i, j)
                    label = "".join(label)
                    records.add(label)
        
        return len(records)
    
    
    def dfs(self, grid, visited, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or i == m or j < 0 or j == n:
            return ["0"]
        
        if grid[i][j] == 0 or visited[i][j]:
            return ["0"]
        
        visited[i][j] = True

        left = self.dfs(grid, visited, i - 1, j)
        right = self.dfs(grid, visited, i + 1, j)
        upp = self.dfs(grid, visited, i, j - 1)
        down = self.dfs(grid, visited, i, j + 1)
            
        res = ["1"]
        res += left
        res += right
        res += upp
        res += down
        
        return res
        
            
        
        
        
        