class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        hMap = {}
        for i in range(lo, hi + 1):
            count = 0
            val = i
            while val != 1:
                if val % 2 == 0:
                    val /= 2
                    count += 1
                elif val % 2 == 1:
                    val = (val * 3) + 1
                    count += 1
            hMap[i] = count
        sorted_keys = sorted(hMap, key=lambda k: hMap[k])
        return sorted_keys[k - 1]