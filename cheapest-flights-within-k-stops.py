class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        def bellman_ford(src):
            dist = [float("inf")] * n
            dist[src] = 0
            
            for _ in range(k+1):
                temp = dist.copy()
                for u, v, w in flights:
                    if dist[u] != float("inf") and dist[u] + w < temp[v]:
                        temp[v] = dist[u] + w
                dist = temp
            
            return dist

        ans = bellman_ford(src)[dst]
        if ans == float('inf'):
            return -1
        return ans