class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        boolean = [None  for _ in range(len(graph))]
        visited = set()
        
        def dfs(each):
            if each in visit:
                return False
            if graph[each] == []:
                return True

            visit.add(each)
            value = True
            for node in graph[each]:
                if boolean[node] == None:
                    boolean[node] = dfs(node)
                value = value & boolean[node]

            return value

        for each in range(len(graph)):
            if each not in visited:
                visited.add(each)
                visit = set()
                boolean[each] = dfs(each)

        answer = []
        for idx in range(len(boolean)):
            if boolean[idx] == True:
                answer.append(idx)

        return answer
        