class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)

        for city1 in range(len(isConnected)):
            for city2 in range(len(isConnected[0])):
                if isConnected[city1][city2] == 1 and city1 != city2:
                    graph[city1 + 1].append(city2 + 1)

        visited = set()
        def dfs(val):
            if val in visited:
                return
                
            visited.add(val)
            
            for values in graph[val]:
                dfs(values)

        answer = 0
        for val in range(1, len(isConnected) + 1):
            if val not in visited:
                answer += 1
                dfs(val)

        return answer