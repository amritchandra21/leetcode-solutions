# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        lowCheck = 1
        upperCheck = n
        while True:
            midCheck = (lowCheck + upperCheck) // 2
            if guess(midCheck) == 1:
                lowCheck = midCheck + 1
            elif guess(midCheck) == -1:
                upperCheck = midCheck - 1
            elif guess(midCheck) == 0:
                return midCheck
