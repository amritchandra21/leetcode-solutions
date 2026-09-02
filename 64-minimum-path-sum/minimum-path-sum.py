class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        minGrid = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]

        for i in range(cols):
            minGrid[rows][i] = float('inf')
        for i in range(rows):
            minGrid[i][cols] = float('inf')
        minGrid[rows][cols - 1] = 0

        for r in range(rows - 1, -1, -1):
            for c in range(cols - 1, -1, -1):
                minGrid[r][c] = grid[r][c] + min(minGrid[r + 1][c], minGrid[r][c + 1])
        return minGrid[0][0]

