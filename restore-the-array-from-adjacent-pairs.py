class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        visited = set()
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            if u not in visited:
                visited.add(u)
            else:
                visited.remove(u)
            if v not in visited:
                visited.add(v)
            else:
                visited.remove(v)

        answer = [0 for _ in range(len(adjacentPairs) + 1)]
        
        for each in visited:
            if answer[0] == 0:
                answer[0] = each
            else:
                answer[-1] = each
        pt = 1
        while pt < len(answer)-1:
            node = answer[pt - 1]
            for each in graph[node]:
                if each not in visited:
                    visited.add(each)
                    answer[pt] = each
            pt += 1

        return answer