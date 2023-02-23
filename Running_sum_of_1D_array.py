class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prev = 0

        for idx in range(len(nums)):
            nums[idx] += prev
            prev = nums[idx]


        return nums
