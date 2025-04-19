class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        def hMap(word):
            freq = {}
            for char in word:
                freq[char] = 1 + freq.get(char, 0)
            return freq

        for r in range(len(s1), len(s2) + 1):
            check = s2[l:r]
            if hMap(check) == hMap(s1):
                return True
            l = l + 1
        return False
            