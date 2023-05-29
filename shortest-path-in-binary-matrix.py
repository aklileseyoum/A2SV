class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        length = len(grid)
        queue = deque([(0, 0, 1)])
        visit = set((0, 0))
        directions = [(1, 1), (1, 0), (0, 1), (-1, 1), (1, -1), (-1, 0), (0, -1), (-1, -1)]

        while queue:
            r, c, leng = queue.popleft()
            if min(r,c) < 0 or max(r, c) >= length or grid[r][c]:
                continue
            if r == length - 1 and c == length - 1:
                return leng

            for dr, dc in directions:
                if (r + dr, c + dc) not in visit:
                    queue.append((r + dr, c + dc, leng + 1))
                    visit.add((r + dr, c + dc))

        return -1