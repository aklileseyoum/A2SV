class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        store = set()
        idx = 0
        indexes = {}
        for a, b in equations:
            store.add(a)
            store.add(b)
            if a not in indexes:
                indexes[a] = idx
                idx += 1
            if b not in indexes:
                indexes[b] = idx
                idx += 1

        n = len(store)
        dist = [[float('inf')] * n for _ in range(n)]
        for idx in range(len(equations)):
            u = indexes[equations[idx][0]]
            v = indexes[equations[idx][1]]
            dist[u][v] = values[idx]
            dist[v][u] = 1 / values[idx]


        for i in range(n):
            dist[i][i] = 1.0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] == float("inf"):
                        dist[i][j] = dist[i][k] * dist[k][j]
       
        answer = []
        for u, v in queries:
            if u not in indexes or v not in indexes or dist[indexes[u]][indexes[v]] == float("inf"):
                answer.append(-1.0)
            else:
                val = dist[indexes[u]][indexes[v]]
                answer.append(val)

        return answer