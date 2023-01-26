class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        output = True
        for row in range(9):
            for col in range(9):
                box = board[row][col]
                if box != '.':
                    count = board[row].count(box)
                    if count > 1:
                        output = False
                    for row2 in range(9):
                        if row2 != row:
                            if box == board[row2][col]:
                                output = False
                    if row <= 2:
                        small_row = 2
                    elif row > 2 and row <=5:
                        small_row = 5
                    else:
                        small_row = 8

                    if col <= 2:
                        small_col = 2
                    elif col > 2 and col <=5:
                        small_col = 5
                    else:
                        small_col = 8

                    start_row = small_row - 2
                    start_col = small_col - 2
                    count = 0
                    for i in range(start_row, small_row+1):
                        count += board[i][start_col:small_col+1].count(box)
                    if count > 1:
                        output = False

                        
        return output
