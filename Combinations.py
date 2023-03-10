class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(current_num, path):
            if current_num > n + 1:
                return 

            if len(path) == k:
                answer.append(path[::])
                return

            path.append(current_num)
            backtrack(current_num + 1, path)
            path.pop()
            backtrack(current_num + 1, path)

        backtrack(1, [])
        return answer