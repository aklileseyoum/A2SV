class Solution:
    def countArrangement(self, n: int) -> int:
        visited = [0 for _ in range(n)]
        count = [0]

        def helper(n, i):
            if i >= n:
                count[-1] += 1
                return

            for j in range(1, n+1):
                if visited[j - 1] == 0 and (j % (i + 1) == 0 or (i + 1) % j == 0):
                    visited[j - 1] = 1
                    helper(n, i+1)
                    visited[j - 1] = 0

        helper(n, 0)
        return count[-1]