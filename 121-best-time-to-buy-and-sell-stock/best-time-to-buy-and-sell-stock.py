class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        maxP = 0
        for r in range(1, len(prices)):
            if prices[l] > prices[r]:
                l = r
            maxP = max(maxP, prices[r] - prices[l])
        return maxP