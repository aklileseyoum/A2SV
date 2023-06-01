class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(amount, idx):
            if amount > target or idx >= len(nums):
                return 0
            if amount == target:
                return 1
            state = (amount, idx)
            if state not in memo:
                x = 0
                for i in range(len(nums)):
                    x += dp(amount+nums[i], idx)
                memo[state] = x

            return memo[state]

        return dp(0, 0)