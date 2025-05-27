class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = collections.deque()
        fresh = 0
        total = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))
        
        while q and fresh > 0:
            length = len(q)
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[1, 0], [0, -1], [0, 1], [-1, 0]]
                for dr, dc in directions:
                    r, c  = row + dr, col + dc
                    if (r in range(len(grid)) and c in range(len(grid[0]))
                    and grid[r][c] == 1):
                        grid[r][c] = 2
                        q.append((r, c))
                        fresh -= 1
            total += 1
        if fresh != 0:
            return -1
        return total