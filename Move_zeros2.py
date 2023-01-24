class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pt1 = 0
        pt2 = 1
        while pt1 < len(nums) and pt2 < len(nums):
            if nums[pt1] == 0 and nums[pt2] != 0:
                nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
                pt1 += 1
                pt2 += 1
            else:
                if nums[pt1] != 0:
                    pt1 += 1
                if nums[pt2] == 0 or nums[pt1-1] != 0:
                    pt2 += 1
