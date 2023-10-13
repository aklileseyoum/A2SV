class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        minimum = nums[0]
        for i in range(1, len(nums)):
            minimum &= nums[i]
        
        ans = 0
        check = nums[0]
        idx = 1
        total = 0
        while idx < len(nums):
            if check + total <= minimum:
                ans += 1
                total += check
                check = nums[idx]
            else:
                check &= nums[idx]
            idx += 1

        if check+total == minimum:
            ans += 1

        return ans