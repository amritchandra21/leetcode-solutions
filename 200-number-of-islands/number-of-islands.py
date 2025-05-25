class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        nOfIslands = 0
        visited = set()

        def bfs(r, c):
            q = collections.deque()
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [0, -1], [0, 1], [-1, 0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if (r in range(len(grid)) and c in range(len(grid[0])) and (r, c) not in visited
                    and grid[r][c] == "1"):
                        visited.add((r, c))
                        q.append((r, c))
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (grid[r][c] == "1" and (r, c) not in visited):
                    bfs(r, c)
                    nOfIslands += 1
        return nOfIslands


