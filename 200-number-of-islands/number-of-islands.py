class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        countIslands = 0
        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))
            directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    ROWS, COLS = dr + row, dc + col
                    if (ROWS in range(rows) and COLS in range(cols) and grid[ROWS][COLS] == "1" and
                    (ROWS, COLS) not in visited):
                        visited.add((ROWS, COLS))
                        q.append((ROWS, COLS))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    countIslands += 1
        return countIslands