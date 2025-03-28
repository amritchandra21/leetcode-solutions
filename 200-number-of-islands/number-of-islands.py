class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        islands = 0
        visited = set()
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    rows, cols = dr + row, dc + col
                    if rows in range(len(grid)) and cols in range(len(grid[0])) and grid[rows][cols] == "1" and (rows, cols) not in visited:
                        visited.add((rows, cols))
                        q.append((rows, cols))
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands

