class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        row, col = entrance
        queue = deque()
        queue.append((row, col, 0))
        maze[row][col] = "+"
        direction = [(1,0), (-1,0), (0,1), (0,-1)]
        while queue:
            r, c, steps = queue.popleft()
            if r == 0 or r == (len(maze) - 1) or c == 0 or c == (len(maze[0]) - 1):
                if steps > 0:
                    return steps

            for dx, dy in direction:
                if 0 <= r + dx < len(maze) and 0 <= c + dy < len(maze[0]) and maze[r+dx][c+dy] == ".":
                    queue.append((r+dx, c+dy, steps+1))
                    maze[r+dx][c+dy] = "+"

        return -1