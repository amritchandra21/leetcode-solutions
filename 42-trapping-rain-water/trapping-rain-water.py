class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        lMax, rMax = height[l], height[r]

        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                res += rMax - height[r]
        return res