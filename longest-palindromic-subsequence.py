class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(s) + 1)]
        s_reversed = s[::-1]
        for row in range(len(s)-1, -1, -1):
            for col in range(len(s)-1, -1, -1):
                if s[row] == s_reversed[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])

        return dp[0][0]