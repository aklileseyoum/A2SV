class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        visited = set()
        
        def dfs(row, col):
            if not ((0 <= row < len(image)) and (0 <= col < len(image[0]))):
                return

            if (row, col) in visited:
                return

            visited.add((row, col))
            if image[row][col] == original:
                image[row][col] = color
            else:
                return
        
            dfs(row + 1, col)
            dfs(row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        dfs(sr, sc)
        return image