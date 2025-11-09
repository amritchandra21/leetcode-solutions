class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minVal = len(nums) + 1
        l = 0
        total = 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minVal = min(minVal, r - l + 1)
                total -= nums[l]
                l += 1

        return 0 if minVal == len(nums) + 1 else minVal