class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dp(idx):
            if idx >= len(cost):
                return 0

            if idx not in memo:
                take_one = dp(idx+1) + cost[idx]
                take_two = 0
                if idx+1 < len(cost):
                    take_two = dp(idx+2) + cost[idx+1]
                memo[idx] = min(take_one, take_two)

            return memo[idx]

        return dp(0)