class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def firstSearch(idx):
            row = set()
            col = set()
            for idx2 in range(len(board)):
                if board[idx2][idx] != '.':
                    if board[idx2][idx] in row:
                        return False
                    row.add(board[idx2][idx])
                
                if board[idx][idx2] != '.':
                    if board[idx][idx2] in col:
                        return False
                    col.add(board[idx][idx2])

            return True

        def secondSearch(row, row2, col, col2):
            visited = set()
            for r in range(row, row2 + 1):
                for c in range(col, col2 + 1):
                    if board[r][c] != '.':
                        if board[r][c] in visited:
                            return False
                        visited.add(board[r][c])
            
            return True



        for idx in range(len(board)):
            if not firstSearch(idx):
                return False


        for row in range(0, len(board), 3):
            for col in range(0, len(board), 3):
                print(row, row+2, col, col+2)
                if not secondSearch(row, row+2, col, col+2):
                    return False

        return True
        
        