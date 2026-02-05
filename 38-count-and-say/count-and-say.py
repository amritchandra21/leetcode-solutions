class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n - 1)
        res = ""
        count = 1
        for i in range(len(prev)):
            if i + 1 < len(prev) and prev[i] == prev[i + 1]:
                count += 1
            else:
                CaS = str(count) + prev[i]
                res += CaS
                count = 1
        return res