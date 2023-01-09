class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        answer = []
        rows = []
        columns = []

        for i in range(len(grid[0])):
            column = 0
            for j in range(len(grid)):
                column += 1 if grid[j][i] else 0
            columns.append(column)

        for row in grid:
            rows.append(sum(row))
        
        for i,row in enumerate(rows):
            new_list = []
            for j,col in enumerate(columns):
                new_list.append(row + col - (len(grid[0]) - row) - (len(grid) - col))
            answer.append(new_list)
            
        return answer
