class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        def bfs(src, dest):
            q = deque([(src, [src])])
            visited = set()
            while q:
                node, path = q.popleft()
                if node == dest:
                    return path

                visited.add(node)
                for n in graph[node]:
                    if n not in visited:
                        q.append((n, path + [n]))
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        freq = defaultdict(int)
        for s, d in trips:
            path = bfs(s, d)
            for node in path:
                freq[node] += 1

        def dp(node, parent, half):
            if (node, parent, half) not in memo:
                if half:
                    cost = freq[node] * (price[node] // 2)
                else:
                    cost = freq[node] * price[node]

                for n in graph[node]:
                    if n != parent:
                        if half:
                            n_cost = dp(n, node, False)
                        else:
                            n_cost = min(dp(n, node, False), dp(n, node, True))
                        cost += n_cost
                memo[(node, parent, half)] = cost
            return memo[(node, parent, half)]   

        cost = float(inf)
        memo = {}
        for node in range(n):
            cost = min(cost, dp(node, None, True), dp(node, None, False))
        return cost