class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(set)
        for one, two in roads:
            graph[one].add(two)
            graph[two].add(one)

        answer = 0
        for city1, city2 in itertools.combinations(graph.keys(), 2):
            if city1 in graph[city2]:
                has_con = 1
            else:
                has_con = 0

            city1_con = len(graph[city1])
            city2_con = len(graph[city2])

            answer = max(answer, city1_con + city2_con - has_con)

        return answer