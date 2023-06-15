class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        def bound(row, col):
            return row < 0 or col < 0 or row == len(grid) or col == len(grid)

        visited = set()
        def dfs(row, col):
            if (bound(row, col) or not grid[row][col] or (row, col) in visited):
                return
            visited.add((row, col))
            for r, c in direction:
                dfs(row+r, col+c)

        def bfs():
            res, queue = 0, deque(visited)
            while queue:
                for i in range(len(queue)):
                    row, col = queue.popleft()
                    for r, c in direction:
                        Row, Col = row + r, col + c
                        if bound(Row, Col) or (Row, Col) in visited:
                            continue
                        if grid[Row][Col]:
                            return res
                        queue.append([Row, Col])
                        visited.add((Row, Col))
                res += 1

        for row in range(len(grid)):
            for col in range(len(grid)):
                if grid[row][col]:
                    dfs(row, col)
                    return bfs()