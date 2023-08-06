class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        ans = [0]
        subsets = []
        def backtrack(idx):
            if idx >= len(requests):
                checker = [[0,0] for _ in range(n)]
                for each in subsets:
                    checker[each[0]][0] += 1
                    checker[each[1]][1] += 1
                yes = True
                for each in checker:
                    if each[0] != each[1]:
                        yes = False
                if yes:
                    ans[-1] = max(len(subsets), ans[-1])
                return

            subsets.append(requests[idx])
            backtrack(idx + 1)
            subsets.pop()
            backtrack(idx + 1)

        backtrack(0)
        return ans[-1]