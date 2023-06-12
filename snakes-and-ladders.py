class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def intToPos(square):
            r = (square - 1) // length
            c = (square - 1) % length
            if r % 2:
                c = length -1 -c
            return [r, c]

        queue = deque()
        queue.append([1,0])
        visited = set()
        while queue:
            square, move = queue.popleft()
            for i in range(1, 7):
                nextsquare = square + i
                r, c = intToPos(nextsquare)
                if board[r][c] != -1:
                    nextsquare = board[r][c]
                if nextsquare == length * length:
                    return move + 1
                if nextsquare not in visited:
                    visited.add(nextsquare)
                    queue.append([nextsquare, move+1])

        return -1