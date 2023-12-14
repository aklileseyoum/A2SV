class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        visited = set()
        ans = 0
        for idx in range(len(mat)):
            ans += mat[idx][idx]
            visited.add((idx, idx))

        idx1 = 0
        idx2 = len(mat) - 1

        while idx1 < len(mat) and idx2 >= 0:
            if (idx1, idx2) not in visited:
                ans += mat[idx1][idx2]
            idx1 += 1
            idx2 -= 1

        return ans
        