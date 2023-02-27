class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum = matrix
        self.prefix_sum.insert(0, [0] * len(matrix[0]))
        for nums in self.prefix_sum:
            nums.insert(0, 0)
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                self.prefix_sum[row][col] = self.prefix_sum[row - 1][col] + self.prefix_sum[row][col -1] - self.prefix_sum[row - 1][col - 1] + self.prefix_sum[row][col]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        answer = self.prefix_sum[row2+1][col2+1] - self.prefix_sum[row2+1][col1] - self.prefix_sum[row1][col2+1] + self.prefix_sum[row1][col1]

        return answer
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
