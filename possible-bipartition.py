class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for dislike in dislikes:
            graph[dislike[0]].append(dislike[1])
            graph[dislike[1]].append(dislike[0])

        seen = {}
        for i in range(n + 1):
            if i not in seen:
                seen[i] = 0
                stack = [i]
                while stack:
                    a = stack.pop()
                    for b in graph[a]:
                        if b in seen:
                            if seen[a] == seen[b]:
                                return False
                        else:
                            seen[b] = (seen[a]+1)%2 
                            stack.append(b)

        return True