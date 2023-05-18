class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = {}      
        for idx in range(len(s1)):
            graph[s1[idx]] = s1[idx]
            graph[s2[idx]] = s2[idx]
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            if xrep != yrep:
                if yrep > xrep:
                    graph[yrep] = xrep
                else:
                    graph[xrep] = yrep

        def find(x):
            if x == graph[x]:
                return x
            graph[x] = find(graph[x])
            return graph[x]
        
        for idx in range(len(s2)):
            union(s1[idx], s2[idx])

        answer = ""
        for each in baseStr:
            if each in graph:
                answer += find(each)
            else:
                answer += each

        return answer