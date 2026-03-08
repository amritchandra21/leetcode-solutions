class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1: 1}

        for num in range(2, n + 1):
            dp[num] = num if num != n else 0
            for i in range(1, num):
                val = dp[i] * dp[num - i]
                dp[num] = max(val, dp[num])
        
        return dp[n]