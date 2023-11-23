class Solution(object):
    def countPairs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        def dfs(node):
            stack = [node]
            visited.add(node)
            connected = 1
            while stack:
                val = stack.pop()
                for each in graph[val]:
                    if each not in visited:
                        stack.append(each)
                        connected += 1
                        visited.add(each)

            return connected

        components = []
        for node in range(n):
            if node not in visited:
                components.append(dfs(node))

        prev = components[-1]
        ans = 0
        for idx in range(len(components) - 2, -1, -1):
            ans += prev * components[idx]
            prev += components[idx]

        return ans
                