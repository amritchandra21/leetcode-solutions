class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dup = set()
        maxLen = 0
        l = 0
        for r in range(len(s)): #pwwkew
            while s[r] in dup:
                dup.remove(s[l])
                l += 1
            maxLen = max(maxLen, r - l + 1)
            dup.add(s[r])
        return maxLen 
