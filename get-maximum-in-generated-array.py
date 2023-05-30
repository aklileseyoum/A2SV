class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = {}
        memo[0] = 0
        memo[1] = 1
        def dp(n):
            if n not in memo:
                memo[n] = dp(n // 2)
                if n % 2 != 0:
                    memo[n] += dp((n // 2) + 1)
            return memo[n]

        answer = []
        for num in range(n + 1):
            answer.append(dp(num))

        return max(answer)