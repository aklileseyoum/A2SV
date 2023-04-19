class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        answer = [[0] for _ in range(len(graph[0]))]
        for i, j in enumerate(graph[0]):
            answer[i].append(j)
        
        store = []
        for idx in range(1, (len(graph) - 1)):
            paths = []
            indexs = []
            for idx2 in range(len(answer)):
                if answer[idx2] and answer[idx2][-1] == idx:
                    paths.append(answer[idx2])
                    indexs.append(idx2)
            
            indexs.sort(reverse = True)
            for i in indexs:
                answer.pop(i)

            if not paths:
                for i in graph[idx]:
                    store.append([idx, i])
        
            for path in paths:
                ans = []
                for i in graph[idx]:
                    added = [i]
                    for each in store:
                        if each[0] == i:
                            added = each
                    ans.append(path + added)
                answer += ans
            
            

        return answer
                