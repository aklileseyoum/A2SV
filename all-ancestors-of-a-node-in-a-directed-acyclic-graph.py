class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        answer = [set() for _ in range(n)]
        graph = defaultdict(list)
        for start, end in edges:
            graph[end].append(start)
            answer[end].add(start)

        def dfs(node):
            val = list(answer[node])
            for each in graph[node]:
                 if each not in visited:
                    dfs(each)
                    visited.add(each)
                 val += list(answer[each])
            answer[node] = set(val)
        
        visited = set()
        for i in range(n):
            dfs(i)

        for i in range(n):
            answer[i] = list(sorted(answer[i]))

        return answer