class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        count = 0
        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid1) or col >= len(grid1[0]) or grid2[row][col] == 0 or (row, col) in visited:
                return True

            visited.add((row, col))
            res = True
            if grid1[row][col] == 0:
                res = False

            res = dfs(row - 1, col) and res
            res = dfs(row + 1, col) and res
            res = dfs(row, col - 1) and res
            res = dfs(row, col + 1) and res

            return res
            
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if grid2[row][col] and (row, col) not in visited and dfs(row, col):
                    count += 1

        return count