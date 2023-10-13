class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        total = [0] * n
        def dfs(node, parent):
            total[node] = values[node]

            for each in graph[node]:
                if each != parent:
                    total[node] += dfs(each, node)

            return total[node]

        dfs(0, -1)
        count = 0
        for each in total:
            if each % k == 0:
                count += 1

        return count