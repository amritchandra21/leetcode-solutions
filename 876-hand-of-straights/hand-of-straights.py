class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cards = {}
        for n in hand:
            cards[n] = 1 + cards.get(n, 0)
        minH = list(cards.keys())
        heapq.heapify(minH)

        while minH:
            first = minH[0]

            for i in range(first, first + groupSize):
                if i not in cards:
                    return False
                cards[i] -= 1
                if cards[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True