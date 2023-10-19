class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        graph = {word: word for word in strs}
        
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
        
        length = len(strs[0])
        for i in range(len(strs)):
            for j in range(i + 1, len(strs)):
                if find(strs[j]) != find(strs[i]) and sum([strs[i][idx] != strs[j][idx] for idx in range(length)]) == 2:
                    union(strs[i], strs[j])

        ans = defaultdict(int)
        for idx in range(len(strs)):
            ans[find(strs[idx])] += 1

        return len(ans)