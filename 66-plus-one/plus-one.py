class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        counter = len(digits) - 1
        if digits[counter] != 9:
            digits[counter] += 1
            return digits
        while digits[counter] == 9:
            digits[counter] = (1 + digits[counter]) % 10
            counter -= 1
        if counter < 0:
            digits.insert(0, 1)
            return digits
        digits[counter] += 1
        return digits