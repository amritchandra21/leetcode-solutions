class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfits = []
        maxCapital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(maxCapital)

        for i in range(k):
            while maxCapital and maxCapital[0][0] <= w:
                c, p = heapq.heappop(maxCapital)
                heapq.heappush(maxProfits, -1 * p)
            if not maxProfits:
                continue
            w += -1 * heapq.heappop(maxProfits)
        return w
            