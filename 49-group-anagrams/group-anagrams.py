class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        final = defaultdict(list)
        for s in strs:
            charCount = [0] * 26
            for c in s:
                charCount[ord(c) - ord("a")] += 1
            final[tuple(charCount)].append(s)

        return list(final.values())