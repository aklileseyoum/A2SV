class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(index, total):
            if index == len(nums):
                if total == target:
                    return 1
                else:
                    return 0

            if (index, total) not in memo:
                memo[(index, total)] = (backtrack(index + 1, total + nums[index]) + backtrack(index + 1, total - nums[index])) 

            return memo[(index, total)]

        return backtrack(0, 0)