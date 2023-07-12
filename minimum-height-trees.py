class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ones = [node for node in graph.keys() if len(graph[node]) == 1]
        
        while n > 2:
            n -= len(ones)
            new = set()
            for one in ones:
                neighbor = graph[one].pop()
                graph[neighbor].remove(one)

                if len(graph[neighbor]) == 1:
                    new.add(neighbor)

            ones = new

        return ones