class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        left, right = 0, 0
        outp = ""
        while left < len(word1) and right < len(word2):
            outp += word1[left]
            outp += word2[right]
            left += 1
            right += 1
        outp += word1[left:]
        outp += word2[right:]
        return outp
