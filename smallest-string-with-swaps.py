class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        rep = {i: i for i in range(len(s))}

        def find(x):
            if x == rep[x]:
                return x

            rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            rx, ry = find(x), find(y)

            if rx != ry:
                if s[rx] < s[ry]:
                    rep[ry] = rx
                else:
                    rep[rx] = ry

        for a, b in pairs:
            union(a, b)

        
        representees = defaultdict(list)

        for i in range(len(s)):
            heapq.heappush(representees[find(i)], s[i])
        
        ans = []
        for i in range(len(s)):
            ans.append(heappop(representees[find(i)]))

        return ''.join(ans)