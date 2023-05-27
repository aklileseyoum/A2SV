class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for first, second in edges:
            graph[first].append(second)
            graph[second].append(first)

        answer = [None] * n
        def dfs(node, parent):
            freq = [0] * 26
            for child in graph[node]:
                if child != parent:
                    f = dfs(child, node)
                    for i in range(26):
                        freq[i] += f[i]

            freq[ord(labels[node]) - ord('a')] += 1
            answer[node] = freq[ord(labels[node]) - ord('a')]
            return freq

        dfs(0, -1)
        return answer