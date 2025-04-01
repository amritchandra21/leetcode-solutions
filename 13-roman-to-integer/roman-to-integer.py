class Solution:
    def romanToInt(self, s: str) -> int:
        RomToInt = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        res = 0
        for c in range(len(s)):
            if c < len(s) - 1 and RomToInt[s[c]] < RomToInt[s[c + 1]]:
                res -= RomToInt[s[c]]
            else:
                res += RomToInt[s[c]]
        return res