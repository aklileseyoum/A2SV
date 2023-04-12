class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        answer = 0
        def dfs(row, col):
            if (row, col) in visited:
                return 

            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])):
                return

            if grid[row][col] == 0:
                return

            visited.add((row, col))
            count[-1] += 1

            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                count = [0]
                if grid[row][col] == 1 and (row, col) not in visited:
                    dfs(row, col)
                    answer = max(answer, count[-1])

        return answer