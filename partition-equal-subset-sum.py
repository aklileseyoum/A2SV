class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False

        target = total // 2
        visited = set()

        def dp(idx, target):
            if target == 0:
                return True

            if target < 0 or idx >= len(nums):
                return False

            if (idx+1, target-nums[idx]) in visited and (idx+1, target) in visited:
                return False

            if dp(idx+1, target-nums[idx]):
                return True
            visited.add((idx+1, target-nums[idx]))

            if dp(idx+1, target):
                return True
            visited.add((idx+1, target))
            

        return dp(0, target)