class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((w, v))

        priority_queue = [(0, k)]
        distance = [float(inf) for _ in range(n)]
        distance[k-1] = 0
        visited = set()
        
        while priority_queue:
            val, node = heapq.heappop(priority_queue)
            if node in visited:
                continue
            visited.add(node)

            for weight, neigh in graph[node]:
                dist = val + weight
                distance[neigh-1] = min(distance[neigh-1], dist)
                heapq.heappush(priority_queue, (dist, neigh))
                
        if max(distance) == float(inf):
            return -1
        return max(distance)