class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        for idx1 in range(len(bombs)):
            x, y, r = bombs[idx1]
            xmin = x - r
            xmax = x + r
            ymin = y - r
            ymax = y + r
            for idx2 in range(len(bombs)):
                if idx1 == idx2:
                    continue
                if (bombs[idx1][2] >= math.sqrt((bombs[idx1][0] - bombs[idx2][0]) ** 2 + (bombs[idx1][1] - bombs[idx2][1]) ** 2)):
                    graph[idx1].append(idx2)

        def dfs(idx):
            stack = [idx]
            ans = 0
            visited = set()
            while stack:
                val = stack.pop(0)
                if val not in visited:
                    visited.add(val)
                    ans += 1
                    val_value = graph[val]
                    stack = val_value + stack

            return ans

        maximum = 0
        for idx in range(len(bombs)):
            maximum = max(maximum, dfs(idx))

        return maximum