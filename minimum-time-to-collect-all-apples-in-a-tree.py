class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        def dfs(node, parent):
            time = 0

            for child in graph[node]:
                if child == parent:
                    continue
                childTime = dfs(child, node)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time

        return dfs(0,  -1)