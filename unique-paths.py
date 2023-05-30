class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        memo[(m-1, n-1)] = 1
        
        def dp(row, col):
            if (row,col) not in memo:
                bottom, right = 0, 0
                if row != m - 1:
                    bottom = dp(row+1, col)
                if col != n - 1:
                    right = dp(row, col+1)
                memo[(row, col)] = right + bottom

            return memo[(row, col)]

        return dp(0, 0)