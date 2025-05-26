class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        count = {}
        for char in s:
            count[char] = 1 + count.get(char, 0)
        maxHeap = []
        for char, freq in count.items():
            maxHeap.append((-freq, char))
        heapq.heapify(maxHeap)
        prev = None
        res = ""
        
        while maxHeap or prev:

            if prev and not maxHeap:
                return ""
            cnt, char = heapq.heappop(maxHeap)
            res += char
            cnt += 1

            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None

            if cnt != 0:
                prev = (cnt, char)
        return res