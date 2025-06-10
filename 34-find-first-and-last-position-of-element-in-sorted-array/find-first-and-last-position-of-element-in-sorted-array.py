class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def leftBias(nums, target, leftB):
            l, r = 0, len(nums) - 1
            res = -1
            while l <= r:
                m = (l + r) // 2
                if target > nums[m]:
                    l = m + 1
                elif target < nums[m]:
                    r = m - 1
                else:
                    res = m
                    if leftB:
                        r = m - 1
                    else:
                        l = m + 1
            return res
        
        l = leftBias(nums, target, True)
        r = leftBias(nums, target, False)
        return [l, r]