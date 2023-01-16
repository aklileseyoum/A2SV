class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ans = []
        for col in range(len(matrix[0])):
            temp = []
            for row in range(len(matrix)-1, -1, -1):
                temp.append(matrix[row][col])
            ans.append(temp)

        matrix.clear()
        matrix.extend(ans)
