class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = {}
        for idx in range(len(accounts)):
            account = accounts[idx]
            for i in range(1, len(account)):
                if account[i] in graph:
                    val = graph[account[i]]
                    for k, v in graph.items():
                        if v == val:
                            graph[k] = idx
                else:
                    graph[account[i]] = idx

        answer = [[] for _ in range(len(accounts))]
        for k, v in graph.items():
            answer[v].append(k)

        ans = []
        for idx in range(len(answer)):
            if len(answer[idx]) >= 1:
                answer[idx].sort()
                answer[idx].insert(0, accounts[idx][0])
                ans.append(answer[idx])

        return ans