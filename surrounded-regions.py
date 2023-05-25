class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def boarder(row, col):
            if row == 0 or col == 0 or row == (len(board)-1) or col == (len(board[0]) - 1):
                return True

        def boundary(row, col):
            if row >= 0 and col >= 0 and row < len(board) and col < len(board[0]):
                return True

        direction = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        change = set()

        def dfs(row, col):
            stack = [(row, col)]
            ans = set()
            flag = True
            while stack:
                row, col = stack.pop(0)
                if boarder(row, col):
                    flag = False
                ans.add((row, col))
                for r, c in direction:
                    if boundary(row+r, col+c) and board[row+r][col+c] == "O" and (row+r, col+c) not in ans:
                        stack = [(row+r, col+c)] + stack

            visited.update(ans)
            if flag:
                change.update(ans)


        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == "O" and (row, col) not in visited:
                    dfs(row, col)

        for r, c in change:
            board[r][c] = "X"