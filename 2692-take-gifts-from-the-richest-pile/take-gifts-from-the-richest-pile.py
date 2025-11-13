class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap = [-g for g in gifts]
        heapq.heapify(maxHeap)
        
        for i in range(k):
            gift = -heapq.heappop(maxHeap)
            newGift = math.isqrt(gift)
            heapq.heappush(maxHeap, -newGift)
        return -sum(maxHeap)
