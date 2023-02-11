class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        temp = [0 for _ in range(8)]
        if len(grid) < 3 and len(grid[0]) < 3:
            return 0

        answer = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[0]) - 2):
                
                summ = set()
                summ.add(grid[row][col] + grid[row][col+1] + grid[row][col+2])
                summ.add(grid[row+1][col] + grid[row+1][col+1] + grid[row+1][col+2])
                summ.add(grid[row+2][col] + grid[row+2][col+1] + grid[row+2][col+2])
                summ.add(grid[row][col] + grid[row+1][col] + grid[row+2][col])
                summ.add(grid[row][col+1] + grid[row+1][col+1] + grid[row+2][col+1])
                summ.add(grid[row][col+2] + grid[row+1][col+2] + grid[row+2][col+2])
                summ.add(grid[row][col] + grid[row+1][col+1] + grid[row+2][col+2])
                summ.add(grid[row][col+2] + grid[row+1][col+1] + grid[row+2][col])
                
                array = set()
                array.add(grid[row][col])
                array.add(grid[row][col+1])
                array.add(grid[row][col+2])
                array.add(grid[row+1][col])
                array.add(grid[row+1][col+1])
                array.add(grid[row+1][col+2])
                array.add(grid[row+2][col])
                array.add(grid[row+2][col+1])
                array.add(grid[row+2][col+2])
                
                compare = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

                if array == compare and len(summ) == 1:
                    answer += 1
        
        return answer
