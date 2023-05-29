class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        queue = []

        for row in range(height):
            for col in range(width):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = "#"

        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for r, c in queue:
            for dx, dy in directions:
                row = r + dx
                col = c + dy

                if 0 <= row < height and 0 <= col < width and mat[row][col] == "#":
                    mat[row][col] = mat[r][c] + 1
                    queue.append((row, col))

        return mat