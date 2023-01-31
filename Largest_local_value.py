class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        length -= 2
        answer = [[0] * length for _ in range(length)]
        for row in range(len(answer)):
            for col in range(len(answer)):
                maximum = 0
                for row1 in range(row, row+3):
                    maxi = max(grid[row1][col:col+3])
                    if maximum < maxi:
                        maximum = maxi

                answer[row][col] = maximum

        return answer
