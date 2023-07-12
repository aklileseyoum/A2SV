class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0

        nums.sort()
        idx1 = 0
        idx2 = len(nums) - 4
        answer = float(inf)

        while idx2 < len(nums):
            answer = min(answer, (nums[idx2] - nums[idx1]))
            idx1 += 1
            idx2 += 1

        return answer