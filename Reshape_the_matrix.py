class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        One_D = []
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                col_len = len(mat[0])
                One_D.append(mat[row][col])

        if len(One_D) // r != c:
            return mat
        answer = [[0] * c for _ in range(r)]
        for i in range(len(One_D)):
            row = i // c
            col = i % c
            answer[row][col] = One_D[i]

        return answer
