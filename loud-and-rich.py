class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        smallest = {i : -1 for i in range(len(quiet))}
        
        for big, small in richer:
            graph[small].append(big)

        def dfs(node):
            if graph[node] == []:
                return node
            mini = quiet[node]
            mini_node = node
            for each in graph[node]:
                if smallest[each] == -1:
                    smallest[each] = dfs(each)
                if mini > quiet[smallest[each]]:
                    mini = quiet[smallest[each]]
                    mini_node = smallest[each]

            return mini_node

        for each in range(len(quiet)):
            if smallest[each] == -1:
                smallest[each] = dfs(each)
        answer = list(smallest.values())
        
        return answer