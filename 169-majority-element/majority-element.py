class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                count = 1
                res = num
            elif num == res:
                count += 1
            elif num != res:
                count -= 1
        return res





        