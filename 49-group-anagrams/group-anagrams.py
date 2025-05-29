class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        final = defaultdict(list)
        for string in strs:
            charCount = [0] * 26
            for c in string:
                charCount[ord(c) - ord("a")] += 1
            final[tuple(charCount)].append(string)

        return final.values()