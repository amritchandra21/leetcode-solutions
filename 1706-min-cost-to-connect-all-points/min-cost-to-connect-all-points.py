from heapq import heappush, heappop
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        seen = set()
        minHeap = [(0, 0)]
        total_count = 0

        while len(seen) < len(points):
            dist, i = heappop(minHeap)
            if i in seen:
                continue
            seen.add(i)
            total_count += dist
            xi, yi = points[i]
            for j in range(len(points)):
                if j not in seen:
                    xj, yj = points[j]
                    new_dist = abs(xj - xi) + abs(yj - yi)
                    heappush(minHeap, (new_dist, j))
        return total_count