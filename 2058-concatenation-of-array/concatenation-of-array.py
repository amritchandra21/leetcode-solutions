class Solution(object):
    def getConcatenation(self, nums):
        newNums = []
        for i in range(0,len(nums) * 2):
            newNums.append(nums[i % len(nums)])
        return newNums
        