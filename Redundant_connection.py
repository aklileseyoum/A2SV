class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        rank = [1]
        for i in range(1, len(edges)+1):
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
            if srep == drep:
                return True
            
            if rank[s] >= rank[d]:
                graph[drep] = srep
                rank[s] += rank[d]
            else:
                graph[srep] = drep
                rank[d] += rank[s]
    
        for s, d in edges:
            if union(s, d):
                return [s, d]
