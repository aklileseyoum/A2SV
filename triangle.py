class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = {}
        ans = float(inf)
        for row in range(len(triangle)):
            for col in range(len(triangle[row])):
                state = (row, col)
                if row == 0:
                    memo[state] = triangle[0][0]
                elif col == 0:
                    memo[state] = memo[(row - 1, col)] + triangle[row][col]
                elif col == len(triangle[row]) - 1:
                    memo[state] = memo[(row - 1, col - 1)] + triangle[row][col]
                else:
                    added = min(memo[(row - 1, col)], memo[(row - 1, col - 1)])
                    memo[state] = added + triangle[row][col]

                if row == len(triangle) - 1:
                    ans = min(ans, memo[state])

        return ans