class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        rank = []
        for i in range(n):
            graph[i] = i
            rank.append(1)

        def find(x):
            if x == graph[x]:
                return x
            graph[x] = find(graph[x])
            return graph[x]

        def union(x, y):
            srep = find(s)
            drep = find(d)
            if srep != drep:
                if rank[s] >= rank[d]:
                    graph[drep] = srep
                    rank[s] += rank[d]
                else:
                    graph[srep] = drep
                    rank[d] += rank[s]

        for s, d in edges:
            union(s, d)
            

        return find(source) == find(destination)