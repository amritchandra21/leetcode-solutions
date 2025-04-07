class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        checker = {}
        for n in nums:
            checker[n] = checker.get(n, 0) + 1
        
        for k, v in checker.items():
            if v == 1:
                return k