class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        points = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                number = matrix[row][col]
                if number == 0:
                    points.append([row,col])

        for point in points:
            row = point[0]
            col = point[1]
            r = 0
            while r < len(matrix):
                matrix[r][col] = 0
                r += 1

            c = 0
            while c < len(matrix[0]):
                matrix[row][c] = 0
                c += 1
