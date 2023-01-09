class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])
        answer = []
        row = col = 0
        up = True
        while len(answer) != rows * cols:
            if up:
                while row >= 0 and col < cols:
                    answer.append(mat[row][col])
                    row -= 1
                    col += 1
                
                if col == cols:
                    col -= 1
                    row += 2
                else:
                    row += 1

                up = False
            else:
                while row < rows and col >= 0:
                    answer.append(mat[row][col])
                    col -= 1
                    row += 1
                if row == rows:
                    col += 2
                    row -= 1
                else:
                    col += 1

                up = True

        return answer
