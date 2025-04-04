class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        cSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in cSet:
                cSet.remove(s[l])
                l += 1
            cSet.add(s[r])
            res = max(res, len(cSet))
        return res