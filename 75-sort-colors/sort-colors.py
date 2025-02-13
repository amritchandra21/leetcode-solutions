class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def swap(l, r):
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
        left, right = 0, len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0:
                swap(left, i)
                left += 1
            elif nums[i] == 2:
                swap(right, i)
                right -= 1
                i -= 1
            i += 1


        