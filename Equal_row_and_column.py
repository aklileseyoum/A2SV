class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        column = []
        for i in range(len(grid)):
            new = []
            for j in range(len(grid)):
                new.append(grid[j][i])
            column.append(new)
        print(column)    
        count = 0
        for row in grid:
            if row in column:
                count += column.count(row)

        return count
