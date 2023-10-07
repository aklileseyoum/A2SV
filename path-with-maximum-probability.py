class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)
        for idx in range(len(edges)):
            graph[edges[idx][0]].append([edges[idx][1], succProb[idx]])
            graph[edges[idx][1]].append([edges[idx][0], succProb[idx]])
        
        def dijkstra(graph, start):
            visited = set()
            priority_queue = [(-1, start)]
            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)
                visited.add(current_node)

                if current_node == end_node:
                    return current_distance * -1

                for neighbor, weight in graph[current_node]:
                    if neighbor not in visited:
                        heapq.heappush(priority_queue, (current_distance * weight, neighbor))
            return 0

        return dijkstra(graph, start_node)