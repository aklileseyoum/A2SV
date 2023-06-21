class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        graph = {}
        def find(x):
            if x != graph[x]:
                graph[x] = find(graph[x])

            return graph[x]

        def union(s, d):
            graph.setdefault(s, s)
            graph.setdefault(d, d)

            srep = find(s)
            drep = find(d)
            if srep != drep:
                graph[drep] = srep 

        for row, col in stones:
            union(row, ~col)

        roots = set()
        for key in graph:
            roots.add(find(key))

        return len(stones) - len(roots)