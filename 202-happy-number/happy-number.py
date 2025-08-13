class Solution:
    def isHappy(self, n: int) -> bool:
        hSet = set()
        def happyCalc(n):
            totSum = 0
            while n  != 0:
                totSum += (n % 10) ** 2
                n = n // 10
            return totSum
        while True:
            n = happyCalc(n)
            if n in hSet:
                return False
            if n == 1:
                return True
            hSet.add(n)
