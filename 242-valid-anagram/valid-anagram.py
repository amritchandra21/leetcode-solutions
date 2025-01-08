class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        countT, countS = {}, {}
        for i in range(0,len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countT == countS

        