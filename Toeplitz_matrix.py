class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        checker = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                number = matrix[row][col]
                difference = row - col
                if difference in checker:
                    if checker[difference] != number:
                        return False
                else:
                    checker[difference] = number

        return True
