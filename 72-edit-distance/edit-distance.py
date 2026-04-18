class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        w1 = len(word1)
        w2 = len(word2)
        dp = [[0 for _ in range(w2 + 1)] for _ in range(w1 + 1)]

        for i in range(w1 + 1):
            dp[i][w2] = w1 - i

        for i in range(w2 + 1):
            dp[w1][i] = w2 - i
        
        for i in range(w1 - 1, -1, -1):
            for j in range(w2 - 1, -1, -1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i + 1][j + 1]
                else:
                    dp[i][j] = 1 + min(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j + 1])

        return dp[0][0]