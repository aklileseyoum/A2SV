class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[1]].append(edge[0])
        
        answer = []
        for ans in range(n):
            if not graph[ans]:
                answer.append(ans)

        return answer