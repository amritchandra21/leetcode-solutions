class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        height, width = len(dungeon), len(dungeon[0])

        n, m = height - 1, width - 1

        dungeon[n][m] = max(1, 1 - dungeon[n][m])
        # [2][2] = 6, [1][2] = 5
        for r in range(n - 1, -1, -1):
            dungeon[r][m] = max(1, dungeon[r + 1][m] - dungeon[r][m])
        
        for c in range(m - 1, -1, -1):
            dungeon[n][c] = max(1, dungeon[n][c + 1] - dungeon[n][c])
        
        for r in range(n - 1, -1, -1):
            for c in range(m - 1, -1, -1):
                dungeon[r][c] = max(1, min(dungeon[r + 1][c], dungeon[r][c + 1]) - dungeon[r][c])
        
        return dungeon[0][0]