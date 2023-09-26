class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        dp = [[0 for col in range(len(dungeon[0]))] for row in range(len(dungeon))]
        for row in range(len(dungeon) - 1, -1, -1):
            for col in range(len(dungeon[0]) -1, -1, -1):
                val = dungeon[row][col]
                if row + 1 == len(dungeon) and col + 1 == len(dungeon[0]):
                    val = dungeon[row][col]
                elif row + 1 == len(dungeon):
                    val += dp[row][col + 1]
                elif col + 1 == len(dungeon[0]):
                    val += dp[row+1][col]
                else:
                    val += max(dp[row+1][col], dp[row][col+1])
                dp[row][col] = min(0, val)

        ans = abs(dp[0][0]) + 1
        return ans