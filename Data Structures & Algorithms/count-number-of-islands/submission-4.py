class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        res = 0

        def dfs(i, j):
            if min(i,j) < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] == "0" or (i, j) in visited:
                return 0
            if grid[i][j] == "1" and (i, j) not in visited:
                visited.add((i, j))
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)    
               
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):      
                if (i, j) not in visited and grid[i][j] == "1":
                    res += 1
                    dfs(i, j)
        return res