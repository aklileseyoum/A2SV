class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def one_round(start, row_end, col_end):
            row = start
            col = start
            half = 0
            count = 0
            iterations = 2 * (row_end - start + 1) + 2 * (col_end - start - 1)
            arr = []
            if iterations == 0:
                arr.append(matrix[row][col])
            elif row_end == 0 or col_end == 0:
                iterations = max(row_end, col_end) + 1
            while count < iterations:
                if row <= row_end and col <= col_end:
                    arr.append(matrix[row][col])
                if half == 0:
                    if col != col_end and row == start:
                        col += 1
                    elif col == col_end and row < row_end:
                        row += 1
                    elif col == col_end and row == row_end:
                        col -= 1
                        half = 1
                else:
                    if col > start:
                        col -= 1
                    elif col == start:
                        row -= 1
                count += 1

            return arr

        
        col_length = len(matrix[0])
        row_length = len(matrix)

        starter = int(min(col_length, row_length) / 2)
        i = 0
        row_end = row_length - 1
        col_end = col_length - 1
        answer = []

        while i <= starter:
            answer += one_round(i, row_end, col_end)
            row_end -= 1
            col_end -= 1
            i += 1
        size = col_length * row_length

        return answer[:size] 