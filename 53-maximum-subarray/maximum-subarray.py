class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        cSum = 0

        for n in nums:
            if cSum < 0:
                cSum = 0
            cSum += n
            maxSum = max(maxSum, cSum)
        
        return maxSum