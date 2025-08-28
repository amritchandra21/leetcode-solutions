class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()

        def dfs(i, j):
            if (i < 0 or j < 0 or i == len(grid)
            or j == len(grid[0]) or grid[i][j] == 0):
                return 1
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            total = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return total
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return dfs(r, c)