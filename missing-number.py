class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new = [-1] * (len(nums) + 1)
        for num in nums:
            new[num] = num

        return new.index(-1)