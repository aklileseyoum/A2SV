class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (-1,1), (1,-1), (-1,-1)]
        answer = board
        def boundary(row, col):
            if row >= 0 and col >= 0 and row < len(board) and col < len(board[0]):
                return True

        def dfs(row, col):
            if board[row][col] != "E":
                return

            bombs = 0
            for r, c in directions:
                if boundary(row+r, col+c) and board[row+r][col+c] == "M":
                    bombs += 1
           
            if bombs:
                board[row][col] = str(bombs)
            else:
                board[row][col] = "B"
                for r, c in directions:
                    if boundary(row+r, col+c):
                        dfs(row+r, col+c)

        row, col = click
        if board[row][col] == "M":
            answer[row][col] = "X"
        else:
            dfs(click[0], click[1])
        return answer