class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        ranges = []
        for idx in range(len(costs)):
            ranges.append([(costs[idx][0] - costs[idx][1]), idx])
        ranges.sort()
        
        ans = 0
        length = len(costs)
        for idx in range(len(ranges)):
            val, i = ranges[idx]
            if idx < length / 2:
                ans += costs[i][0]
            else:
                ans += costs[i][1]

        return ans
        