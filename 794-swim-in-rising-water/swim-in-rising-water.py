class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        height = len(grid)
        seen = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        minHeap = [[grid[0][0], 0, 0]]
        seen.add((0, 0))
        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == height - 1 and c == height - 1:
                return t
            for dr, dc in directions:
                newR, newC = dr + r, dc + c
                if (newR < 0 or newC < 0 or newR == height or newC == height
                or (newR, newC) in seen):
                    continue
                seen.add((newR, newC))
                heapq.heappush(minHeap, [max(t, grid[newR][newC]), newR, newC])